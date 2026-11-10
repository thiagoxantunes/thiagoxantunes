# Analisador de Cortes para Vídeos Curtos com IA

<!-- resumo: Ferramenta que usa IA para encontrar os melhores trechos de vídeos longos e gerar cortes para TikTok, Reels e Shorts. -->
<!-- stack: JavaScript, HTML/CSS, IA generativa, Node.js (docx) -->
<!-- status: Protótipo -->

## O problema

Transformar um episódio de podcast de mais de 1 hora em dezenas de vídeos curtos exige assistir tudo, anotar timestamps e escrever títulos e legendas um por um.

## A solução

Uma ferramenta web interativa que:

- Recebe o link do vídeo e as preferências (tipo de momento, duração de 15–30 s, quantidade);
- Analisa a **transcrição** com IA e devolve os cortes com **timestamp de início e fim**, título, frase-gancho, justificativa e **score de potencial viral (0–100)**;
- Permite **filtrar por categoria** (humor, história, impacto, reação, reflexão);
- Abre o vídeo direto no momento do corte e copia os timestamps com um clique;
- **Exporta** todos os cortes em `.txt` para uso em editores (CapCut, Opus Clip);
- Um script em **Node.js** gera um documento Word com título, descrição e hashtags otimizados para cada corte.

## Resultado

Em um episódio de teste, foram identificados **50 cortes** prontos para edição, o suficiente para mais de 3 semanas de postagens diárias. Também foi criado um guia passo a passo de edição no CapCut (formato 9:16, legenda automática, exportação em 1080p).

## Aprendizados

- O YouTube bloqueia a busca de transcrições direto do navegador; a solução foi separar a obtenção da transcrição da etapa de análise;
- Estrutura de saída em JSON para a IA facilita renderizar e filtrar os resultados.

> Uso recomendado apenas com conteúdo próprio ou com autorização do criador original.

## Competências demonstradas

JavaScript · Integração com IA · UX de ferramentas internas · Automação de conteúdo
