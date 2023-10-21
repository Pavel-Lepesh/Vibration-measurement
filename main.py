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
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # разметка сайдбара
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # кнопки на сайдбаре
        self.coefficient_image = customtkinter.CTkImage(Image.open('images/coefficient.png'), size=(30, 30))
        self.coefficient_button = customtkinter.CTkButton(self.sidebar_frame,
                                                          text="Коэффициенты",
                                                          image=self.coefficient_image,
                                                          corner_radius=0,
                                                          anchor="w",
                                                          font=customtkinter.CTkFont(family='Courier New',
                                                                                     size=15),
                                                          fg_color="transparent",
                                                          text_color=("gray10", "gray90"),
                                                          border_spacing=10,
                                                          )
        self.coefficient_button.grid(row=3, sticky="we")

        # лого и тайтл на сайдбаре
        self.logo_image = customtkinter.CTkImage(Image.open('images/logo_image.png'), size=(160, 100))

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                 text='Vibration',
                                                 font=customtkinter.CTkFont(family='Courier New', size=20, weight='bold'),
                                                 image=self.logo_image,
                                                 compound="top")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 100))

        # основное окно приложения и его разметка
        self.insert_items_frame = customtkinter.CTkFrame(self, fg_color="#B0C4DE", corner_radius=10)
        self.insert_items_frame.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=20, pady=10)
        self.insert_items_frame.grid_columnconfigure(list(range(13)), weight=1)
        self.insert_items_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # создаем 13 фреймов для подшипников в основном окне
        self.frame_items = []
        for i in range(13):
            for j in range(4):
                item_frame = customtkinter.CTkFrame(self.insert_items_frame, fg_color='#6495ED', corner_radius=10, border_color='black', border_width=1)
                item_frame.grid(row=j, column=i, padx=2, pady=2, sticky="nsew")
                item_frame.grid_rowconfigure(0, weight=1)
                item_frame.grid_rowconfigure(1, weight=4)
                item_frame.grid_columnconfigure(0, weight=1)
                self.frame_items.append(item_frame)

        # создаем названия и фреймы для столбцов значений на фреймах подшипников
        self.label_items = []
        self.values_frames = []
        for i in range(13):
            item_frame = self.frame_items[i]
            item_label = customtkinter.CTkLabel(item_frame,
                                                text=f'№{i + 1}',
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
            label_a = customtkinter.CTkLabel(value_frame, text='Амплитуда', width=1, font=self.main_font)
            label_f = customtkinter.CTkLabel(value_frame, text='Фаза', width=1, font=self.main_font)
            label_a.grid(row=0, column=0, padx=1, pady=1)
            label_f.grid(row=0, column=1, padx=1, pady=1)
            for j in range(1, 4):
                item_entry_amp = customtkinter.CTkEntry(value_frame)
                item_entry_amp.grid(row=j, column=0, sticky='we')
                item_entry_f = customtkinter.CTkEntry(value_frame)
                item_entry_f.grid(row=j, column=1, sticky='ew')

        # # фрейм для дополнительных данных
        # self.additional_data_frame = customtkinter.CTkFrame(self.insert_items_frame, fg_color='#2F4F4F', corner_radius=10)
        # self.additional_data_frame.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
        # self.additional_data_frame.grid_rowconfigure(0, weight=1)
        # self.additional_data_frame.grid_rowconfigure(1, weight=3)
        # self.additional_data_frame.grid_columnconfigure(0, weight=1)
        #
        # label_add_data_frame = customtkinter.CTkLabel(self.additional_data_frame,
        #                                               text='Данные',
        #                                               fg_color='#FFFFF0',
        #                                               width=150,
        #                                               corner_radius=10,
        #                                               font=self.main_font)
        # label_add_data_frame.grid(row=0, padx=20, pady=10, sticky="ns")
        # self.value_add_data_frame = customtkinter.CTkFrame(self.additional_data_frame, fg_color="transparent")
        # self.value_add_data_frame.grid(row=1, padx=20, pady=0, sticky="nswe")
        # self.value_add_data_frame.grid_rowconfigure((0, 1, 2), weight=1)
        # self.value_add_data_frame.grid_columnconfigure((0, 1), weight=1)
        #
        # for i, name in enumerate(['Груз', 'Угол', 'Фазовая\nпоправка']):
        #     label_data = customtkinter.CTkLabel(self.value_add_data_frame,
        #                                         text=name,
        #                                         width=50,
        #                                         text_color='white',
        #                                         font=self.main_font)
        #     label_data.grid(row=i, column=0, padx=5, pady=5)
        #     inputs = customtkinter.CTkEntry(self.value_add_data_frame, width=50)
        #     inputs.grid(row=i, column=1, padx=5, pady=5)
        #
        # # кнопка для расчета результата
        # self.result_button = customtkinter.CTkButton(self.insert_items_frame,
        #                                              text='Расчет',
        #                                              fg_color='green',
        #                                              height=50,
        #                                              font=self.main_font)
        # self.result_button.grid(row=2, column=4)


if __name__ == '__main__':
    app = App()
    app.mainloop()
