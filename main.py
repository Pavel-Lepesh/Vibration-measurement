import customtkinter
import logging
from PIL import Image


logging.basicConfig(level=logging.INFO)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Vibration')
        self.main_font = customtkinter.CTkFont(family='Courier New')

        # настраиваем разметку для всего приложения
        self.geometry(f"{1100}x{580}")
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # окно для вкладок
        self.top_panel = customtkinter.CTkFrame(self, fg_color='#B0C4DE', corner_radius=10, border_color='black', border_width=1, height=40)
        self.top_panel.grid(row=0, column=1, sticky='we', padx=10, pady=1)
        #self.top_panel.grid_columnconfigure(list(range(8)), weight=1)
        self.button_cof = customtkinter.CTkButton(self.top_panel, text='Коэффициенты', height=10)
        self.button_cof.grid(row=0, column=0, pady=2, padx=[10, 2], sticky='w')
        self.button_cargo = customtkinter.CTkButton(self.top_panel, text='Груз', height=10)
        self.button_cargo.grid(row=0, column=1, pady=2, padx=2, sticky='w')

        # окно для данных
        self.data_panel = customtkinter.CTkFrame(self, fg_color='#B0C4DE', corner_radius=10, border_color='black', border_width=1, height=40)
        self.data_panel.grid(row=1, column=1, sticky='ew', padx=10, pady=1)
        for i, name in zip([0, 2, 4], ['Груз', 'Угол', 'Фазовая\nпоправка']):
            label = customtkinter.CTkLabel(self.data_panel, text=name, fg_color='#4682B4', width=50, corner_radius=5)
            label.grid(row=0, column=i, padx=10, pady=2)

        for i in [1, 3, 5]:
            entry_window = customtkinter.CTkEntry(self.data_panel, width=50)
            entry_window.grid(row=0, column=i, padx=10, pady=2)

        self.result_button = customtkinter.CTkButton(self.data_panel, text='Расчет', fg_color='#228B22')
        self.result_button.grid(row=0, column=6)

        # основное окно приложения и его разметка
        self.insert_items_frame = customtkinter.CTkFrame(self, fg_color="#B0C4DE", corner_radius=10)
        self.insert_items_frame.grid(row=2, column=1, sticky="nsew", padx=10, pady=1)
        #self.insert_items_frame.grid_columnconfigure(0, weight=1)
        self.insert_items_frame.grid_columnconfigure(list(range(14)), weight=1)
        self.insert_items_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # создаем 14 фреймов для подшипников в основном окне
        self.frame_items = []
        for i in range(3):
            for j in range(14):
                item_frame = customtkinter.CTkFrame(self.insert_items_frame, fg_color='#6495ED', corner_radius=10, border_color='black', border_width=1)
                item_frame.grid(row=i, column=j, padx=1, pady=2, sticky="nsew")
                item_frame.grid_rowconfigure(0, weight=1)
                item_frame.grid_rowconfigure(1, weight=4)
                item_frame.grid_columnconfigure(0, weight=1)
                self.frame_items.append(item_frame)

        # создаем названия и фреймы для столбцов значений на фреймах подшипников
        self.label_items = []
        self.values_frames = []
        for i in range(1, 14):
            item_frame = self.frame_items[i]
            item_label = customtkinter.CTkLabel(item_frame,
                                                text=f'№{i}',
                                                fg_color='#FFFFF0',
                                                width=150,
                                                corner_radius=10,
                                                font=self.main_font,
                                                text_color="black")
            item_label.grid(row=0, padx=20, pady=10, sticky="n")
            self.label_items.append(item_label)

            value_frame = customtkinter.CTkFrame(item_frame, fg_color='transparent', corner_radius=10)
            value_frame.grid(row=1, padx=1, pady=10, sticky="nsew")
            value_frame.grid_columnconfigure((0, 1), weight=1)
            self.values_frames.append(value_frame)

        # создаем input окна для амплитуд и фаз
        for i in range(13):
            value_frame = self.values_frames[i]
            label_a = customtkinter.CTkLabel(value_frame, text='Ампли\nтуда', width=1, font=self.main_font)
            label_f = customtkinter.CTkLabel(value_frame, text='Фаза', width=1, font=self.main_font)
            label_a.grid(row=0, column=0, padx=1, pady=1)
            label_f.grid(row=0, column=1, padx=1, pady=1)
            for j in range(1, 4):
                item_entry_amp = customtkinter.CTkEntry(value_frame)
                item_entry_amp.grid(row=j, column=0, sticky='we')
                item_entry_f = customtkinter.CTkEntry(value_frame)
                item_entry_f.grid(row=j, column=1, sticky='ew')


        # второй ряд
        self.label_items2 = []
        self.values_frames2 = []
        for i in range(15, 28):
            item_frame = self.frame_items[i]
            item_label = customtkinter.CTkLabel(item_frame,
                                                text=f'№{i - 14}',
                                                fg_color='#FFFFF0',
                                                width=150,
                                                corner_radius=10,
                                                font=self.main_font,
                                                text_color="black")
            item_label.grid(row=0, padx=20, pady=10, sticky="n")
            self.label_items2.append(item_label)

            value_frame = customtkinter.CTkFrame(item_frame, fg_color='transparent', corner_radius=10)
            value_frame.grid(row=1, padx=1, pady=10, sticky="nsew")
            value_frame.grid_columnconfigure((0, 1), weight=1)
            self.values_frames2.append(value_frame)

        for i in range(13):
            value_frame = self.values_frames2[i]
            label_a = customtkinter.CTkLabel(value_frame, text='Ампли\nтуда', width=1, font=self.main_font)
            label_f = customtkinter.CTkLabel(value_frame, text='Фаза', width=1, font=self.main_font)
            label_a.grid(row=0, column=0, padx=1, pady=1)
            label_f.grid(row=0, column=1, padx=1, pady=1)
            for j in range(1, 4):
                item_entry_amp = customtkinter.CTkEntry(value_frame)
                item_entry_amp.grid(row=j, column=0, sticky='we')
                item_entry_f = customtkinter.CTkEntry(value_frame)
                item_entry_f.grid(row=j, column=1, sticky='ew')

        # третий ряд
        self.label_items3 = []
        self.values_frames3 = []
        for i in range(29, 42):
            item_frame = self.frame_items[i]
            item_frame.configure(fg_color='#3CB371')
            item_label = customtkinter.CTkLabel(item_frame,
                                                text=f'№{i - 28}',
                                                fg_color='#FFFFF0',
                                                width=150,
                                                corner_radius=10,
                                                font=self.main_font,
                                                text_color="black")
            item_label.grid(row=0, padx=20, pady=10, sticky="n")
            self.label_items3.append(item_label)

            value_frame = customtkinter.CTkFrame(item_frame, fg_color='transparent', corner_radius=10)
            value_frame.grid(row=1, padx=1, pady=10, sticky="nsew")
            value_frame.grid_columnconfigure((0, 1), weight=1)
            self.values_frames3.append(value_frame)

        for i in range(13):
            value_frame = self.values_frames3[i]
            label_a = customtkinter.CTkLabel(value_frame, text='Ампли\nтуда', width=1, font=self.main_font)
            label_f = customtkinter.CTkLabel(value_frame, text='Фаза', width=1, font=self.main_font)
            label_a.grid(row=0, column=0, padx=1, pady=1)
            label_f.grid(row=0, column=1, padx=1, pady=1)
            for j in range(1, 4):
                item_entry_amp = customtkinter.CTkEntry(value_frame)
                item_entry_amp.grid(row=j, column=0, sticky='we')
                item_entry_f = customtkinter.CTkEntry(value_frame)
                item_entry_f.grid(row=j, column=1, sticky='ew')

        # third_row_title = self.frame_items[28]
        # label_for_third_row = customtkinter.CTkLabel(third_row_title, text='r')
        # label_for_third_row.grid(row=0)

        first_row_title = self.frame_items[0]
        label_for_first_row = customtkinter.CTkLabel(first_row_title, text='1')
        label_for_first_row.grid(row=0)

        second_row_title = self.frame_items[14]
        label_for_second_row = customtkinter.CTkLabel(second_row_title, text='2')
        label_for_second_row.grid(row=0)




if __name__ == '__main__':
    app = App()
    app.mainloop()
