from playwright.sync_api import sync_playwright
import os

def run(playwright):
    # Define o caminho para salvar o estado do usuário
    user_data_dir = "./user_data_dir"
    
    # Verifica se o diretório já existe, se não, cria
    if not os.path.exists(user_data_dir):
        os.makedirs(user_data_dir)

    # Inicia o navegador com as configurações para salvar o estado
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir,
        headless=False,  # Defina como True se não quiser ver o navegador
    )

    # Cria uma nova página
    page = browser.new_page()

    # Navega até o WhatsApp Web
    page.goto("https://web.whatsapp.com")

    # Aqui você pode adicionar lógica adicional para verificar se já está logado
    # Por exemplo, esperar por um elemento que só aparece quando logado
    logged_in = page.locator('.two').is_visible(timeout=60000)
    
    if logged_in:
        print("Já está logado no WhatsApp Web!")
    else:
        print("Por favor, escaneie o código QR para fazer login.")
        # Espera até que o login seja concluído
        page.wait_for_selector('.two', timeout=300000)  # 5 minutos de timeout
        print("Login realizado com sucesso!")

    # Aqui você pode adicionar mais código para interagir com o WhatsApp Web

    # Mantém o navegador aberto até que o usuário pressione Enter
    input("Pressione Enter para fechar o navegador...")

    # Fecha o navegador
    browser.close()
    
    # Irei rodar um while true que irá realizar leituras 
    # constantes da fila de tarefa no arquivo do banco de dados
    # E será controlado com base nas tarefas lá informadas

# Executa o script
with sync_playwright() as playwright:
    run(playwright)