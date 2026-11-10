# Documentação Técnica e Acadêmica em LaTeX

<!-- resumo: Conversão de especificações em Markdown para LaTeX no padrão ABNT, com tabelas de casos de uso e referências BibTeX. -->
<!-- stack: LaTeX, BibTeX, Markdown, ABNT -->
<!-- status: Concluído -->

## Sobre

Ao longo do TCC, padronizei a documentação técnica do sistema em **LaTeX**:

- Conversão de documentos escritos em **Markdown** para LaTeX;
- Tabelas de **casos de uso** com `longtable`/`tabularx`, com fluxos principal, alternativos (`A1.1`, `A1.2`…) e de exceção (`E1.1`…) que quebram linha corretamente dentro das células;
- Rótulos e referências cruzadas (`\label`, `\ref`) para cada caso de uso;
- Gestão de referências com **BibTeX** (`\cite{...}`) no padrão **ABNT**, com levantamento e verificação das fontes e páginas citadas.

## Exemplo

```latex
\subsection{Caso de Uso: Gerenciar Processos de Estágio}
\label{uc:fun01}
\textbf{Identificação:} UC-FUN-01
% Tabela com Nome, Ator(es), Descrição, Pré-condição, Fluxos...
```

## Competências demonstradas

LaTeX · Documentação técnica · Normas ABNT · Pesquisa bibliográfica
