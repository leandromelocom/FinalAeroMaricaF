
import sqlite3
from tkinter import *
import messagebox
from tkinter import ttk
import sqlite3
#from PIL import Image, ImageTk


class LoginApp():
    def __init__(self,master=None):
        self.root = root
        self.root.title("LOGIN - Login de Funcionário e Cadastro de Funcionário")
        self.root.geometry('800x300+400+100')
        self.root.configure(background='#c21f40')
        self.frame_pri()
    def frame_pri(self):
        """
        image_path = "img/aeroporto_marica.jpg"
        image = Image.open(image_path)

        width, height = 800, 300
        image.thumbnail((width, height))
        photo = ImageTk.PhotoImage(image)

        self.frame_0 = Label(self.root,image=photo)
        self.frame_0.place(relx=0.01, rely=0.03, relwidth=0.55, relheight=0.95)
        """
        self.label_titulo = Label(self.root, text="Aero Maricá".upper(),font='arial 20 bold',background='#c21f40')
        self.label_titulo.place(relx=0.66, rely=0.03, relwidth=0.25, relheight=0.10)

        self.label_username = Label(self.root, text="Funcionário".upper(),font='arial 10 bold',background='#c21f40')
        self.label_username.place(relx=0.63, rely=0.19, relwidth=0.14, relheight=0.10)

        self.entry_username = Entry(root,font='verdana 10 bold',bg='lightgray')
        self.entry_username.place(relx=0.63, rely=0.30, relwidth=0.30, relheight=0.10)
        
        self.label_password = Label(root, text="senha".upper(),font='arial 10 bold',background='#c21f40')
        self.label_password.place(relx=0.63, rely=0.49, relwidth=0.08, relheight=0.10)

        self.entry_password = Entry(root, show="*",font='verdana 10 bold',bg='lightgray')
        self.entry_password.place(relx=0.63, rely=0.60, relwidth=0.30, relheight=0.10)
        
        self.button_login = Button(root, text="Login".upper(), command=self.login,bg='lightgray')
        self.button_login.place(relx=0.63, rely=0.80, relwidth=0.10, relheight=0.10)
        
        self.button_cadastrar = Button(root, text="Cadastrar".upper(), command=self.register,bg='lightgray')
        self.button_cadastrar.place(relx=0.83, rely=0.80, relwidth=0.10, relheight=0.10)
        
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.create_table()

        root.mainloop()
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL
            )
        """)
        self.conn.commit()
    
    def register(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        
        if username and password:
            self.cursor.execute("""
                INSERT INTO users (username, password) VALUES (?, ?)
            """, (username, password))
            self.conn.commit()
            
            messagebox.showinfo(f"Logado com sucesso", "Funcionario {username} Logado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor entrar com o nome do Funcionrio e senha.")
    
    def login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        
        if username and password:
            self.cursor.execute("""
                SELECT * FROM users WHERE username = ? AND password = ?
            """, (username, password))
            user = self.cursor.fetchone()
            
            if user:
                messagebox.showinfo("Logado com sucesso", "Funcionario: {} Logado com sucesso!".format(username).upper())
                self.root.destroy()
                self.open_cadastro_voo()
            else:
                messagebox.showerror("Erro", "Nome ou senha Invalida.")
        else:
            messagebox.showerror("Erro", "Por favor entrar com o nome do Funcionrio e senha.")
    
    def open_cadastro_voo(self):
        
        root = Tk()

        class Funcoes():
            def limpa_tela(self):
                self.entry_codigo.delete(0,END)
                self.entry_numero_voo.delete(0,END)
                self.entry_aeronave.delete(0,END)
                self.entry_data.delete(0,END)
                self.entry_destino.delete(0,END)
                self.entry_piloto.delete(0,END)

            def conecta_bd(self):
                self.conn = sqlite3.connect('voe_marica.bd')
                self.cursor = self.conn.cursor()

                print('Conectado oa Banco Voe Maricá')
            
            def desconecta_bd(self):
                self.conn.close()

            def monta_tabelas(self):
                self.conecta_bd()
                print('Banco Desconectado')

            # Criar Tabelas
                self.cursor.execute(""" 
                                    CREATE TABLE IF NOT EXISTS registro (
                                        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                                        numero_voo VARCHAR(25) NOT NULL,
                                        aeronave VARCHAR(50),
                                        data VARCHAR(20),
                                        destino VARCHAR(30),
                                        piloto VARCHAR(30)
                                        )
                                    """)

                self.conn.commit(); print('Tabela Registro Criada')
                self.desconecta_bd()

            def variaveis(self):
                self.codigo = self.entry_codigo.get().strip()
                self.numero_voo = self.entry_numero_voo.get().strip().title()
                self.aeronave = self.entry_aeronave.get().strip().title()
                self.data = self.entry_data.get().strip().title()
                self.destino = self.entry_destino.get().strip().title()
                self.piloto = self.entry_piloto.get().strip().title()

            def carregar_valores_iniciais(self):
                self.conecta_bd()

                self.cursor.execute("SELECT DISTINCT numero_voo FROM registro ORDER BY numero_voo")
                voo = [row[0] for row in self.cursor.fetchall()]
                self.entry_numero_voo['values'] = voo

                self.cursor.execute("SELECT DISTINCT aeronave FROM registro ORDER BY aeronave")
                aeronave = [row[0] for row in self.cursor.fetchall()]
                self.entry_aeronave['values'] = aeronave

                self.cursor.execute("SELECT DISTINCT data FROM registro ORDER BY data")
                data = [row[0] for row in self.cursor.fetchall()]
                self.entry_data['values'] = data

                self.cursor.execute("SELECT DISTINCT destino FROM registro ORDER BY destino")
                destino = [row[0] for row in self.cursor.fetchall()]
                self.entry_destino['values'] = destino

                self.cursor.execute("SELECT DISTINCT piloto FROM registro ORDER BY piloto")
                piloto = [row[0] for row in self.cursor.fetchall()]
                self.entry_piloto['values'] = piloto

                self.desconecta_bd()

            def add_voo(self):
                self.variaveis()
                self.conecta_bd()

                self.cursor.execute("""
                                    INSERT INTO registro(numero_voo,aeronave,data,destino,piloto)
                                    VALUES (?,?,?,?,?)""",
                                    (self.numero_voo,self.aeronave,self.data,self.destino,self.piloto))
                self.conn.commit()

                self.cursor.execute("SELECT DISTINCT numero_voo FROM registro ORDER BY numero_voo")
                voo = [row[0] for row in self.cursor.fetchall()]
                self.entry_numero_voo['values'] = voo

                self.cursor.execute("SELECT DISTINCT aeronave FROM registro ORDER BY aeronave")
                aeronave = [row[0] for row in self.cursor.fetchall()]
                self.entry_aeronave['values'] = aeronave

                self.cursor.execute("SELECT DISTINCT data FROM registro ORDER BY data")
                data = [row[0] for row in self.cursor.fetchall()]
                self.entry_data['values'] = data

                self.cursor.execute("SELECT DISTINCT destino FROM registro ORDER BY destino")
                destino = [row[0] for row in self.cursor.fetchall()]
                self.entry_destino['values'] = destino

                self.cursor.execute("SELECT DISTINCT piloto FROM registro ORDER BY piloto")
                piloto = [row[0] for row in self.cursor.fetchall()]
                self.entry_piloto['values'] = piloto

                self.desconecta_bd()
                self.select_lista()
                
                self.limpa_tela()


            def select_lista(self):
                self.lista_voo.delete(*self.lista_voo.get_children())
                self.conecta_bd()
                lista = self.cursor.execute("""
                                        SELECT codigo, numero_voo, aeronave, data, destino, piloto 
                                        FROM registro
                                        ORDER BY codigo DESC""")
                for i in lista:
                    self.lista_voo.insert('','end', values=i)

                self.desconecta_bd()

            def OnDoubleClick(self,event):
                self.limpa_tela()
                self.lista_voo.selection()
                
                for n in self.lista_voo.selection():
                    col1,col2,col3,col4,col5,col6 = self.lista_voo.item(n, 'values')
                    
                    self.entry_codigo.insert(END,col1)
                    self.entry_numero_voo.insert(END,col2)
                    self.entry_aeronave.insert(END,col3)
                    self.entry_data.insert(END,col4)
                    self.entry_destino.insert(END,col5)
                    self.entry_piloto.insert(END,col6)
                    
            def deleta_voo(self):
                self.variaveis()
                self.conecta_bd()
                self.cursor.execute("""
                                        DELETE FROM registro WHERE codigo = ? """,(self.codigo,))
                self.conn.commit()   
                self.desconecta_bd()
                self.limpa_tela()
                self.select_lista()

            def alterar(self):
                self.variaveis()
                self.conecta_bd()

                self.cursor.execute(""" UPDATE registro SET codigo=?, numero_voo=?, aeronave=?, data=?, destino=?, piloto=?
                                        WHERE codigo = ? """,
                                        (self.codigo,self.numero_voo,self.aeronave,self.data,self.destino,self.piloto,self.codigo))

                self.conn.commit()
                
                self.desconecta_bd()
                self.select_lista()
                self.limpa_tela() 

            def busca_numero_voo(self):
                self.conecta_bd()
                self.lista_voo.delete(*self.lista_voo.get_children())
                self.entry_numero_voo.insert(END,'')
                voo = self.entry_numero_voo.get().strip()
                self.cursor.execute(""" SELECT codigo, numero_voo, aeronave, data, destino, piloto  
                                        FROM registro
                                        WHERE numero_voo
                                        LIKE '%%%s%%' ORDER BY numero_voo ASC""" % voo)
                buscavoo = self.cursor.fetchall()
                for i in buscavoo:
                    self.lista_voo.insert("",END,values=i)
                    #self.limpa_tela()
                    self.desconecta_bd()


            def busca_data(self):
                self.conecta_bd()
                self.lista_voo.delete(*self.lista_voo.get_children())
                self.entry_data.insert(END,'')
                data = self.entry_data.get().strip()
                self.cursor.execute(""" SELECT codigo, numero_voo, aeronave, data, destino, piloto  
                                        FROM registro
                                        WHERE data
                                        LIKE '%%%s%%' ORDER BY data ASC""" % data)
                buscadata = self.cursor.fetchall()
                for i in buscadata:
                    self.lista_voo.insert("",END,values=i)
                    #self.limpa_tela()
                    self.desconecta_bd()

       

        class Validadores:
                def validate_entry2(self,text):
                        if text == "": return True
                        try:
                                value = int(text)
                        except ValueError:
                                return False
                                return 0 <= value <= 100000000000000


        class Application(Funcoes,Validadores):
            def __init__(self,master=None):
                self.root = root
                self.validaEntrada()
                self.tela()
                self.frames()
                self.widgts()
                self.lista_frame3()
                self.monta_tabelas()
                self.carregar_valores_iniciais()
                self.select_lista()

                root.mainloop()

            def tela(self):
                self.root.title('')
                largura_tela = root.winfo_screenwidth()
                altura_tela = root.winfo_screenheight()
                self.root.geometry("%dx%d+0+0" % (largura_tela, altura_tela))
                self.root.configure(background='gray')
                self.root.minsize(width=400,height=300)

            def frames(self):

                self.frame_1 = Frame(self.root,bd= 4,highlightbackground='black',highlightthickness=2,bg='#066699')
                self.frame_1.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.12)

                self.frame_2 = Frame(self.root, bd= 4,highlightbackground='black',highlightthickness=2,bg='#195e63')
                self.frame_2.place(relx=0.01, rely=0.14, relwidth=0.98, relheight=0.40)

                self.frame_3 = Frame(self.root, bd= 4,highlightbackground='black',highlightthickness=2 ,bg='#195e63')
                self.frame_3.place(relx=0.01, rely=0.55, relwidth=0.98, relheight=0.44)

            def create_label(self,text,font,bg,fg,relx=None,rely=None,relwidth=None,relheight=None):
                label = Label(self.frame_2,text=text,font=font,bg=bg,fg=fg)
                if relx is not None and rely is not None and relwidth is not None and relheight is not None:
                    label.place(relx=relx,rely=rely,relwidth=relwidth,relheight=relheight)
                return label
            
            def create_entry(self,font,relx=None,rely=None,relwidth=None,relheight=None):
                entry = ttk.Combobox(self.frame_2,font=font)
                if relx is not None and rely is not None and relwidth is not None and relheight is not None:
                    entry.place(relx=relx,rely=rely,relwidth=relwidth,relheight=relheight)
                return entry
            
            def create_botao(self,text,font,bg,command,relx=None,rely=None,relwidth=None,relheight=None):
                botao = Button(self.frame_2,text=text,font=font,bg=bg,command=command)
                if relx is not None and rely is not None and relwidth is not None and relheight is not None:
                    botao.place(relx=relx,rely=rely,relwidth=relwidth,relheight=relheight)
                return botao
            
            def widgts(self):
                
            # Titulo
                self.label_titulo = Label(self.frame_1, background= '#066699',text='cadastro aero Maricá'.upper(), font='verdana 40 bold')
                self.label_titulo.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
            # ID
                
                self.label_codigo = self.create_label('código'.upper(),'verdana 12 bold','#195e63','white',0.04,0.05,0.06,0.06)
                self.entry_codigo = ttk.Entry(self.frame_2,font='verdana 12 bold',validatecommand=self.vcmd2)
                self.entry_codigo.place(relx=0.11, rely=0.04, relwidth=0.10, relheight=0.08)
           
                self.label_numero_voo = self.create_label('nº voo'.upper(),'verdana 12 bold','#195e63','white',0.05,0.21,0.05,0.06)
                self.entry_numero_voo = self.create_entry('verdana 12',0.11,0.20,0.10,0.08)  
           
                self.label_aeronave = self.create_label('aeronave'.upper(),'verdana 12 bold','#195e63','white',0.02,0.36,0.08,0.06)
                self.entry_aeronave = self.create_entry('verdana 12',0.11,0.35,0.20,0.08)
            
                self.label_data = self.create_label('data'.upper(), 'verdana 12 bold','#195e63','white',0.06,0.51,0.04,0.06)
                self.entry_data = self.create_entry('verdana 12',0.11,0.50,0.10,0.08)
            
                self.label_destino = self.create_label('destino'.upper(),'verdana 12 bold','#195e63','white',0.03,0.66,0.07,0.06)
                self.entry_destino = self.create_entry('verdana 12',0.11,0.65,0.20,0.08)
          
                self.label_piloto = self.create_label('piloto'.upper(),'verdana 12 bold','#195e63','white',0.04,0.81,0.06,0.06)
                self.entry_piloto = self.create_entry('verdana 12',0.11,0.80,0.20,0.08)
            
                self.bt_salvar = self.create_botao('salvar'.upper(),'verdana 10 bold','lightblue',self.add_voo,0.60,0.05,0.10,0.15)
            
                self.bt_alterar = self.create_botao('alterar'.upper(),'verdana 10 bold','lightblue',self.alterar,0.60,0.25,0.10,0.15)
            
                self.bt_limpar = self.create_botao('limpar'.upper(),'verdana 10 bold','lightblue',self.limpa_tela,0.60,0.45,0.10,0.15)
            
                self.bt_excluir = self.create_botao('excluir'.upper(),'verdana 10 bold','lightblue',self.deleta_voo,0.60,0.65,0.10,0.15)
            
                self.bt_busca_numero_voo = self.create_botao('busca por nº do voo'.upper(),'verdana 8 bold','lightgray',self.busca_numero_voo,0.40,0.25,0.14,0.10)
            
                self.bt_busca_data = self.create_botao('busca por data'.upper(),'verdana 8 bold','lightgray',self.busca_data,0.40,0.45,0.14,0.10)
           
                self.bt_refresh = self.create_botao('recarregar tabela'.upper(),'verdana 8 bold','lightgreen',self.select_lista,0.40,0.05,0.14,0.10)

            def lista_frame3(self):
                self.style = ttk.Style()
                self.style.theme_use('clam') # alt, default,clam, vista
                self.style.configure('Treeview',background='gray',foreground='black',
                                                        rowheight=30,fieldbackground='gray')
                self.style.map('Treeview',background=[('selected','#012677')])
                        
                self.lista_voo = ttk.Treeview(self.frame_3,selectmode='extended',show='headings',height=3,columns=('col1','col2','col3','col4','col5','col6'))
                self.lista_voo.heading('#0',text='')
                self.lista_voo.heading('#1', text='Código')
                self.lista_voo.heading('#2', text='Numero Voo')
                self.lista_voo.heading('#3', text='Aeronave')
                self.lista_voo.heading('#4', text='Data')
                self.lista_voo.heading('#5', text='Destino')
                self.lista_voo.heading('#6', text='Piloto')
                
                self.lista_voo.column('#0',width=0)
                self.lista_voo.column('#1', width=30)
                self.lista_voo.column('#2', width=100)
                self.lista_voo.column('#3', width=200)
                self.lista_voo.column('#4', width=50)
                self.lista_voo.column('#5', width=200)
                self.lista_voo.column('#6', width=100)
                self.lista_voo.place(relx=0.01,rely=0.01,relwidth=0.97,relheight=0.95)

            # Barra de Rolagem
                self.scroollista = Scrollbar(self.frame_3,orient='vertical')
                self.lista_voo.configure(yscroll= self.scroollista.set)
                self.scroollista.place(relx=0.98,rely=0.01,relwidth=0.02,relheight=0.95)
                self.lista_voo.bind('<Double-1>',self.OnDoubleClick)

            def validaEntrada(self):
                self.vcmd2 = (self.root.register(self.validate_entry2), "%P")


        Application()
    

if __name__ == '__main__':
    root = Tk()
    login_app = LoginApp(root)
    root.mainloop()

