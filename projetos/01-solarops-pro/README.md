# SolarOps Pro — ERP/SaaS para Empresas de Energia Solar

<!-- resumo: Plataforma SaaS que integra comercial, operação, monitoramento e financeiro de uma empresa de energia solar. -->
<!-- stack: Next.js 15, TypeScript, Supabase, ShadCN UI, Zustand, TanStack Query, GitHub Actions -->
<!-- status: Em produção -->

> Desenvolvido para a operação real da **J3 Energia**.

## O problema

A empresa usava planilhas e ferramentas separadas para vender, instalar, monitorar usinas e controlar o financeiro, sem visão única do negócio.

## O que o sistema faz

- **Comercial**: prospecção, propostas com cálculo de payback e ROI, calculadora solar, kits, catálogo de produtos e ordens de serviço
- **Operação**: cadastro de clientes e usinas, monitoramento de geração, alertas com severidade e manutenções preventivas/corretivas
- **Financeiro completo**: contas a pagar/receber, fluxo de caixa, DRE, conciliação bancária, extratos, cartões, contratos, inadimplentes, notas fiscais, estoque, fechamento de obras e espelho de ponto
- Fluxo de **aprovações** financeiras e controle de acesso por perfil (RLS no Supabase)
- Geração de PDF (propostas/relatórios) com `@react-pdf/renderer`
- **10 workflows de GitHub Actions**: CI, testes, backup semanal, coleta diária dos portais de geração, alertas agendados, envio de faturas por e-mail, notificações diárias e health-check pós-deploy

## Tecnologias

Next.js 15 · TypeScript · Supabase · ShadCN UI · Zustand · TanStack Query · GitHub Actions

## Competências demonstradas

Arquitetura full-stack · Modelagem de banco de dados · Regras de negócio financeiras · CI/CD · Automação

## Links

- Repositório: privado (código disponível sob solicitação)
- Demonstração / capturas de tela: `[adicionar]`
