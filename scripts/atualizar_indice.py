#!/usr/bin/env python3
"""Regera a tabela de projetos do README.md principal.

Lê cada projetos/*/README.md e usa:
  - o primeiro título "# ..." como nome
  - os comentários <!-- resumo: ... -->, <!-- stack: ... --> e <!-- status: ... -->

Uso:  python3 scripts/atualizar_indice.py
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
README = RAIZ / "README.md"
INICIO = "<!-- INICIO-PROJETOS (gerado por scripts/atualizar_indice.py — não edite à mão) -->"
FIM = "<!-- FIM-PROJETOS -->"


def campo(texto, nome):
    m = re.search(rf"<!--\s*{nome}:\s*(.*?)\s*-->", texto)
    return m.group(1).strip() if m else ""


def main():
    linhas = ["| Projeto | Descrição | Tecnologias | Status |", "|---|---|---|---|"]
    pastas = sorted(p for p in (RAIZ / "projetos").iterdir() if (p / "README.md").exists())
    for pasta in pastas:
        texto = (pasta / "README.md").read_text(encoding="utf-8")
        titulo = re.search(r"^#\s+(.+)$", texto, re.M)
        nome = titulo.group(1).strip() if titulo else pasta.name
        link = f"projetos/{pasta.name}/"
        linhas.append(
            f"| [**{nome}**]({link}) | {campo(texto, 'resumo')} | "
            f"{campo(texto, 'stack')} | {campo(texto, 'status')} |"
        )

    conteudo = README.read_text(encoding="utf-8")
    padrao = re.compile(re.escape(INICIO) + r".*?" + re.escape(FIM), re.S)
    novo = f"{INICIO}\n" + "\n".join(linhas) + f"\n{FIM}"
    README.write_text(padrao.sub(lambda _: novo, conteudo), encoding="utf-8")
    print(f"Índice atualizado com {len(pastas)} projeto(s).")


if __name__ == "__main__":
    main()
