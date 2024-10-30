def calcular_razao_bissetriz(lado_b, lado_c, tipo="interna"):
    """
    Calcula a razão entre os segmentos formados pela bissetriz (interna ou externa) no lado oposto.
    
    Parâmetros:
    - lado_b: comprimento do lado oposto ao vértice C.
    - lado_c: comprimento do lado oposto ao vértice B.
    - tipo: tipo de bissetriz ("interna" ou "externa").
    
    Retorna:
    - A razão BD/DC conforme o tipo de bissetriz selecionado.
    """
    if lado_b <= 0 or lado_c <= 0:
        return "Os lados devem ser maiores que zero."
    
    if tipo == "interna":
        # Razão para a bissetriz interna
        razao = lado_b / lado_c
    elif tipo == "externa":
        # Razão para a bissetriz externa (inverso da interna)
        razao = lado_c / lado_b
    else:
        return "Tipo de bissetriz invalido. Use 'interna' ou 'externa'."
    
    return razao

# Teste de exemplo
lado_b = 0  # Insira o valor do lado oposto a C
lado_c = 0  # Insira o valor do lado oposto a B
tipo = "interna"  # Altere para "externa" para testar a bissetriz externa

# Executa o cálculo
resultado = calcular_razao_bissetriz(lado_b, lado_c, tipo)
print(f"A razao BD/DC para a bissetriz {tipo} é {resultado}")
