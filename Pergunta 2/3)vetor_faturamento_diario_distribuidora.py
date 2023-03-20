"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que
desejar, que calcule e retorne:
    • O menor valor de faturamento ocorrido em um dia do mês;
    • O maior valor de faturamento ocorrido em um dia do mês;
    • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
    a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
    b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no
    cálculo da média;

"""
import json

# carrega os dados do arquivo JSON
with open('dados.json') as arquivo:
    dados = json.load(arquivo)

# inicializa as variáveis
menor_faturamento = float('inf')
maior_faturamento = float('-inf')
total_faturamento = 0
dias_com_faturamento = 0
dias_acima_da_media = 0

# percorre os dados
for dia in dados:
    valor = dia['valor']
    if dia['valor'] > 0:
        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor

        dias_com_faturamento += 1
        total_faturamento += valor

# calcula a média mensal de faturamento
media_mensal = total_faturamento / dias_com_faturamento

# conta o número de dias com faturamento acima da média
for dia in dados:
    if dia['valor'] > media_mensal:
        dias_acima_da_media += 1

# exibe os resultados
print(f'Menor faturamento: R$ {menor_faturamento:.2f}')
print(f'Maior faturamento: R$ {maior_faturamento:.2f}')
print(f'{dias_acima_da_media} dias com faturamento acima da média mensal de R$ {media_mensal:.2f}')
