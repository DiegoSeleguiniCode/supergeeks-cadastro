import tkinter as tk
from tkinter import messagebox, Listbox
from backend import adicionar_usuario, listar_usuarios, inicializar_banco

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuários")
        
        # Criar um menu
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Menu de Cadastro
        menu_cadastro = tk.Menu(menu_bar, tearoff=0)
        menu_cadastro.add_command(label="Cadastrar", command=self.mostrar_cadastro)
        menu_cadastro.add_command(label="Visualizar", command=self.mostrar_visualizacao)
        menu_bar.add_cascade(label="Menu", menu=menu_cadastro)

        # Frame de Cadastro
        self.frame_cadastro = tk.Frame(self.root)
        tk.Label(self.frame_cadastro, text="Nome:").pack(pady=5)
        self.entry_nome = tk.Entry(self.frame_cadastro)
        self.entry_nome.pack(pady=5)

        tk.Label(self.frame_cadastro, text="E-mail:").pack(pady=5)
        self.entry_email = tk.Entry(self.frame_cadastro)
        self.entry_email.pack(pady=5)

        tk.Label(self.frame_cadastro, text="Telefone:").pack(pady=5)
        self.entry_telefone = tk.Entry(self.frame_cadastro)
        self.entry_telefone.pack(pady=5)

        tk.Label(self.frame_cadastro, text="Nota (0 a 10):").pack(pady=5)
        self.entry_nota = tk.Entry(self.frame_cadastro)
        self.entry_nota.pack(pady=5)

        # Botão de cadastro
        btn_adicionar = tk.Button(self.frame_cadastro, text="Cadastrar", command=self.cadastrar_usuario)
        btn_adicionar.pack(pady=10)

        # Frame de Visualização
        self.frame_visualizacao = tk.Frame(self.root)
        self.listbox_usuarios = Listbox(self.frame_visualizacao, width=70)
        self.listbox_usuarios.pack(pady=10)

        # Inicializar o banco de dados
        inicializar_banco()

        # Mostrar tela de cadastro ao iniciar
        self.mostrar_cadastro()

    def cadastrar_usuario(self):
        """Cadastra um novo usuário."""
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        telefone = self.entry_telefone.get()
        nota = self.entry_nota.get()

        resultado = adicionar_usuario(nome, email, telefone, nota)
        messagebox.showinfo("Resultado", resultado)

        # Limpar campos
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)

    def listar_usuarios(self):
        """Lista os usuários no Listbox."""
        usuarios = listar_usuarios()
        self.listbox_usuarios.delete(0, tk.END)  # Limpar a lista antes de adicionar os usuários
        for usuario in usuarios:
            self.listbox_usuarios.insert(tk.END, f"Nome: {usuario[0]}, E-mail: {usuario[1]}, Telefone: {usuario[2]}, Nota: {usuario[3]}")

    def mostrar_cadastro(self):
        """Mostra o frame de cadastro."""
        self.frame_cadastro.pack(fill=tk.BOTH, expand=True)
        self.frame_visualizacao.pack_forget()

    def mostrar_visualizacao(self):
        """Mostra o frame de visualização e lista usuários."""
        self.frame_visualizacao.pack(fill=tk.BOTH, expand=True)
        self.frame_cadastro.pack_forget()
        self.listar_usuarios()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
