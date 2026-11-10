# Como atualizar este portfólio

## Primeira vez: publicar no GitHub

1. Crie um repositório **público** no GitHub com o **mesmo nome do seu usuário** (ex.: se o usuário é `thiagoantunes`, o repositório é `thiagoantunes/thiagoantunes`). Assim o `README.md` aparece direto na página do seu perfil.
2. Na pasta deste portfólio, rode:

```bash
git init
git add .
git commit -m "Portfólio inicial"
git branch -M main
git remote add origin https://github.com/thiagoxantunes/thiagoxantunes.git
git push -u origin main
```

3. No `README.md`, troque o link do LinkedIn (`linkedin.com/in/thiago-antunes-5bb029201`) e `SEU-EMAIL` pelos seus dados.

## Adicionar um projeto novo

```bash
./scripts/novo_projeto.sh nome-do-projeto     # cria projetos/18-nome-do-projeto/README.md
# preencha o README (resumo, stack e status ficam nos comentários do topo)
python3 scripts/atualizar_indice.py           # atualiza a tabela de projetos
git add . && git commit -m "Adiciona projeto: nome-do-projeto" && git push
```

## Atualizar o LinkedIn

1. Abra `linkedin/LINKEDIN.md`;
2. Adicione a entrada do projeto novo na seção **Projetos** (mesmo texto do resumo do README);
3. No LinkedIn: **Perfil → Adicionar seção → Projetos**, cole o texto e coloque o link da pasta do projeto no GitHub;
4. (Opcional) publique um post usando o **modelo da seção 6**.

## Checklist rápido

- [ ] README do projeto com problema, solução, resultado e tecnologias
- [ ] Nenhuma senha, token ou dado de cliente no repositório
- [ ] Índice atualizado (`atualizar_indice.py`)
- [ ] Linha do tempo do README principal atualizada
- [ ] Projeto adicionado no LinkedIn

## Seus repositórios estão em várias contas

Hoje os projetos estão espalhados em contas diferentes do GitHub (`atnsx`, `atnsxxx`, `thiaguinhooxavier-lgtm`, `beatrizfxantunes-bot`); a conta principal é **thiagoxantunes**. Para o portfólio ficar mais forte:

1. Escolha **uma conta principal** (a que vai no LinkedIn);
2. Transfira os repositórios para ela: **Settings → Danger Zone → Transfer ownership** em cada repositório;
3. Antes de deixar um repositório **público**, confira que `.env`, `.env.local` e chaves (`*.keystore`) **não** estão versionados (`git ls-files | grep -E "env|keystore"`);
4. Atualize os links na seção **Links** de cada projeto.
