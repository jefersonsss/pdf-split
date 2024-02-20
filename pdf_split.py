import PyPDF2

def dividir_pdf(input_path, output_path, paginas_por_arquivo):
    with open(input_path, 'rb') as arquivo_original:
        leitor_pdf = PyPDF2.PdfReader(arquivo_original)
        numero_de_paginas = len(leitor_pdf.pages)

        for i in range(0, numero_de_paginas, paginas_por_arquivo):
            intervalo_paginas = slice(i, i + paginas_por_arquivo)
            novo_pdf = PyPDF2.PdfWriter()
            
            for pagina in leitor_pdf.pages[intervalo_paginas]:
                novo_pdf.add_page(pagina)
            
            with open(f"{output_path}/arquivo_{i // paginas_por_arquivo + 1}.pdf", 'wb') as novo_arquivo:
                novo_pdf.write(novo_arquivo)

if __name__ == "__main__":
    arquivo_entrada = 'C:/pdf/original.pdf'
    diretorio_saida = 'C:/pdf/saida'
    paginas_por_arquivo = 5

    dividir_pdf(arquivo_entrada, diretorio_saida, paginas_por_arquivo)
