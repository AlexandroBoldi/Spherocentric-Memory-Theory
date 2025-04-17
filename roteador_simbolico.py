# Seleção simbólica de rotas com fallback alternativo
def selecionar_rota(zonas, obstaculos):
    for zona in zonas:
        if zona['id'] not in obstaculos:
            return zona['id']
    return 'Rota Emergencial'