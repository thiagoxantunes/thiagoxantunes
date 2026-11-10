#!/usr/bin/env bash
# Cria a pasta de um novo projeto a partir do template.
# Uso: ./scripts/novo_projeto.sh nome-do-projeto
set -euo pipefail
cd "$(dirname "$0")/.."

if [ $# -lt 1 ]; then
  echo "Uso: $0 nome-do-projeto"; exit 1
fi

ultimo=$(ls projetos | grep -oE '^[0-9]+' | sort -n | tail -1 || echo 0)
num=$(printf "%02d" $((10#${ultimo:-0} + 1)))
pasta="projetos/${num}-$1"

mkdir -p "$pasta"
cp templates/PROJETO.md "$pasta/README.md"
echo "Criado: $pasta/README.md"
echo "1) Preencha o README  2) Rode: python3 scripts/atualizar_indice.py  3) git add . && git commit && git push"
