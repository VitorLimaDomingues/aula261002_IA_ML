from reportlab.lib.pagesizes import letter 
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle  
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib import colors

def gerar_pdf(filename="relatorio.pdf"):
    
    doc = SimpleDocTemplate(filename, pagesize = letter, rightMargin = 40, topMargin= 40, bottomMargin= 40)
    
    styles = getSampleStyleSheet();
    
    story = []
    
    story.append(Paragraph("<b> Controle de Estoque:<\b> Módulo de Exportação PDF", styles['Heading1']))
    story.append(Paragraph("<b> Desenvolvedores:<\b> Leonardo Mesquita e Vitor de Lima Domingues", styles['Normal']))
    story.append(Spacer(1, 5))
    
    quantidade = [54, 32, 12, 76, 43, 87, 37]
    valorUnitario = [40, 12, 43, 10, 3, 7, 23]
    
    data = [
        ["Suprimentos", "Quantidade", "Preço/unidade", "Valor do Estoque"],
        ["Nuggets", f"{quantidade[0]} unidades", f"{valorUnitario[0]}", f"R$ {quantidade[0] * valorUnitario[0]},"],
        ["Coca-Cola", f"{quantidade[1]} unidades", f"{valorUnitario[1]}", f"R$ {quantidade[1] * valorUnitario[1]},"],
        ["Açaí", f"{quantidade[2]} unidades", f"{valorUnitario[2]}", f"R$ {quantidade[2] * valorUnitario[2]},"],
        ["Monster", f"{quantidade[3]} unidades", f"{valorUnitario[3]}", f"R$ {quantidade[3] * valorUnitario[3]},"],
        ["Sonho de Valsa", f"{quantidade[4]} unidades", f"{valorUnitario[4]}", f"R$ {quantidade[4] * valorUnitario[4]},"],
        ["Amendoim", f"{quantidade[5]} unidades", f"{valorUnitario[5]}", f"R$ {quantidade[5] * valorUnitario[5]},"],
        ["Leite em Pó", f"{quantidade[6]} unidades", f"{valorUnitario[6]}", f"R$ {quantidade[6] * valorUnitario[6]},"],
    ]