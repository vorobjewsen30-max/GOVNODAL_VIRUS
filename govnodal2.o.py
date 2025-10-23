import os
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import winshell
from win32com.client import Dispatch
from PIL import Image, ImageTk
import ctypes
import time
import threading
import random

class GOVNOOSInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("GOVNO OS Installer")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.installation_cancelled = False
        
        self.show_installation()
        
    def show_installation(self):
        # Создаем основной canvas для анимации
        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Запускаем процесс установки
        self.installation_thread = threading.Thread(target=self.installation_process)
        self.installation_thread.daemon = True
        self.installation_thread.start()
        
        # Создаем кнопку отмены (скрытую)
        self.cancel_btn = tk.Button(self.root, text="Нажмите CAPSLOCK для отмены", 
                                  font=('Segoe UI', 12), bg='red', fg='white',
                                  command=self.cancel_installation)
        self.cancel_btn.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        
        # Привязываем CapsLock
        self.root.bind('<KeyPress-Caps_Lock>', lambda e: self.cancel_installation())
        self.root.focus_set()
        
    def installation_process(self):
        try:
            # Этап 1: Подготовка
            self.show_stage("Инициализация установки GOVNO OS", "Подготовка системы...")
            time.sleep(2)
            
            if self.installation_cancelled: return
            
            # Этап 2: Форматирование диска
            self.show_stage("Форматирование диска", "Очистка GOVNO_DISK...")
            self.show_disk_animation()
            time.sleep(3)
            
            if self.installation_cancelled: return
            
            # Этап 3: Копирование файлов
            self.show_stage("Копирование файлов GOVNO OS", "Установка системных компонентов...")
            self.show_file_copy_animation()
            time.sleep(4)
            
            if self.installation_cancelled: return
            
            # Этап 4: Настройка системы
            self.show_stage("Настройка системы", "Оптимизация производительности...")
            self.show_progress_animation()
            time.sleep(3)
            
            if self.installation_cancelled: return
            
            # Этап 5: Перезагрузка
            self.show_stage("Завершение установки", "Подготовка к перезагрузке...")
            time.sleep(2)
            
            if self.installation_cancelled: return
            
            # Показываем экран перезагрузки
            self.show_reboot_screen()
            
        except Exception as e:
            print(f"Ошибка установки: {e}")
            
    def show_stage(self, title, description):
        self.canvas.delete("all")
        
        # Логотип GOVNO OS
        self.canvas.create_text(960, 200, text="💩", font=('Arial', 80), fill='#00ff00', tags="logo")
        self.canvas.create_text(960, 300, text="GOVNO OS", font=('Segoe UI', 36, 'bold'), fill='white', tags="title")
        self.canvas.create_text(960, 350, text=title, font=('Segoe UI', 18), fill='#cccccc', tags="subtitle")
        
        # Описание этапа
        self.canvas.create_text(960, 450, text=description, font=('Segoe UI', 14), fill='#888888', tags="desc")
        
        # Прогресс бар
        self.canvas.create_rectangle(560, 550, 1360, 580, outline='#333333', fill='#222222', tags="progress_bg")
        
        self.root.update()
        
    def show_disk_animation(self):
        # Анимация форматирования диска
        disk_info = [
            "Форматирование раздела C:...",
            "Создание раздела GOVNO_DISK...",
            "Оптимизация таблицы разделов...",
            "Проверка целостности данных...",
            "Настройка файловой системы GOVNO_FS..."
        ]
        
        for i, info in enumerate(disk_info):
            if self.installation_cancelled: return
            
            self.canvas.delete("disk_info")
            self.canvas.create_text(960, 500, text=info, font=('Segoe UI', 12), fill='#00ff00', tags="disk_info")
            
            # Анимация прогресса
            progress_width = 800 * (i + 1) / len(disk_info)
            self.canvas.create_rectangle(560, 550, 560 + progress_width, 580, fill='#00ff00', outline='', tags="progress")
            
            self.root.update()
            time.sleep(0.8)
            
    def show_file_copy_animation(self):
        # Анимация копирования файлов
        files = [
            "kernel.govno",
            "system32/govno.dll",
            "drivers/ponos.sys",
            "bin/shitutils.exe",
            "lib/govnolib.so",
            "config/govnoconf.cfg"
        ]
        
        for i, file in enumerate(files):
            if self.installation_cancelled: return
            
            self.canvas.delete("file_info")
            status = f"Копирование: {file}"
            self.canvas.create_text(960, 480, text=status, font=('Consolas', 11), fill='#00ff00', tags="file_info")
            
            # Случайный прогресс
            progress_width = 800 * (i + 1) / len(files)
            self.canvas.delete("progress")
            self.canvas.create_rectangle(560, 550, 560 + progress_width, 580, fill='#00ff00', outline='', tags="progress")
            
            # Случайная скорость
            speed = random.randint(50, 200)
            speed_text = f"Скорость: {speed} MB/s"
            self.canvas.create_text(960, 520, text=speed_text, font=('Consolas', 10), fill='#888888', tags="speed")
            
            self.root.update()
            time.sleep(0.5)
            
    def show_progress_animation(self):
        # Анимация настройки системы
        tasks = [
            "Установка компонентов GOVNO...",
            "Настройка реестра...",
            "Оптимизация производительности...",
            "Создание пользовательских настроек...",
            "Финализация установки..."
        ]
        
        for i, task in enumerate(tasks):
            if self.installation_cancelled: return
            
            self.canvas.delete("task_info")
            self.canvas.create_text(960, 480, text=task, font=('Segoe UI', 12), fill='#00ff00', tags="task_info")
            
            progress_width = 800 * (i + 1) / len(tasks)
            self.canvas.delete("progress")
            self.canvas.create_rectangle(560, 550, 560 + progress_width, 580, fill='#00ff00', outline='', tags="progress")
            
            self.root.update()
            time.sleep(0.7)
            
    def show_reboot_screen(self):
        self.canvas.delete("all")
        
        # Экран перезагрузки
        self.canvas.create_text(960, 400, text="GOVNO OS", font=('Segoe UI', 48, 'bold'), fill='#00ff00')
        self.canvas.create_text(960, 480, text="Установка завершена успешно!", font=('Segoe UI', 18), fill='white')
        self.canvas.create_text(960, 520, text="Перезагрузка системы...", font=('Segoe UI', 14), fill='#cccccc')
        
        # Анимация загрузки
        for i in range(10):
            if self.installation_cancelled: return
            
            dots = "." * (i % 4)
            self.canvas.delete("loading")
            self.canvas.create_text(960, 560, text=f"Загрузка{dots}", font=('Consolas', 12), fill='#00ff00', tags="loading")
            self.root.update()
            time.sleep(0.5)
            
        # Запускаем GOVNO OS Desktop
        if not self.installation_cancelled:
            self.root.after(100, self.start_govno_os)
            
    def start_govno_os(self):
        # Закрываем установщик и запускаем GOVNO OS
        self.root.destroy()
        govno_root = tk.Tk()
        GOVNOOSDesktop(govno_root)
        govno_root.mainloop()
        
    def cancel_installation(self):
        self.installation_cancelled = True
        self.canvas.delete("all")
        self.canvas.create_text(960, 400, text="Установка отменена", font=('Segoe UI', 24), fill='red')
        self.canvas.create_text(960, 450, text="Возврат к Windows...", font=('Segoe UI', 14), fill='white')
        self.root.update()
        time.sleep(2)
        self.root.destroy()

class GOVNOOSDesktop:
    def __init__(self, root):
        self.root = root
        self.root.title("GOVNO OS")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='#1a1a1a')
        
        # Привязываем CapsLock для выхода
        self.root.bind('<KeyPress-Caps_Lock>', lambda e: self.exit_govno_os())
        self.root.focus_set()
        
        self.create_desktop()
        
    def create_desktop(self):
        # Фоновое изображение (можно заменить на своё)
        self.bg_label = tk.Label(self.root, bg='#1a1a1a')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Иконки на рабочем столе
        desktop_icons = [
            ("💩", "Мой GOVNO", 100, 100),
            ("🗑️", "Корзина", 100, 200),
            ("🔧", "Настройки", 100, 300),
            ("🌐", "GOVNO Browser", 100, 400),
            ("🎮", "Игры", 100, 500)
        ]
        
        for icon, text, x, y in desktop_icons:
            icon_frame = tk.Frame(self.root, bg='#1a1a1a')
            icon_frame.place(x=x, y=y)
            
            icon_label = tk.Label(icon_frame, text=icon, font=('Arial', 24), 
                                bg='#1a1a1a', fg='white', cursor='hand2')
            icon_label.pack()
            
            text_label = tk.Label(icon_frame, text=text, font=('Segoe UI', 9), 
                                bg='#1a1a1a', fg='white', cursor='hand2')
            text_label.pack()
            
            # Привязываем клики
            icon_label.bind('<Button-1>', lambda e, t=text: self.icon_click(t))
            text_label.bind('<Button-1>', lambda e, t=text: self.icon_click(t))
        
        # Панель задач
        taskbar = tk.Frame(self.root, bg='#2d2d2d', height=40)
        taskbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Кнопка Пуск GOVNO OS
        start_btn = tk.Label(taskbar, text="💩 ПУСК", font=('Segoe UI', 10, 'bold'), 
                           bg='#0078d4', fg='white', cursor='hand2', padx=15, pady=8)
        start_btn.pack(side=tk.LEFT, padx=5)
        start_btn.bind('<Button-1>', lambda e: self.show_start_menu())
        
        # Время
        time_label = tk.Label(taskbar, text="GOVNO OS", font=('Segoe UI', 9), 
                            bg='#2d2d2d', fg='white', padx=10)
        time_label.pack(side=tk.RIGHT)
        
        # Подсказка
        hint_label = tk.Label(self.root, text="Нажмите CAPSLOCK для выхода из GOVNO OS", 
                            font=('Segoe UI', 12), bg='#1a1a1a', fg='#666666')
        hint_label.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
        
    def icon_click(self, icon_name):
        messages = {
            "Мой GOVNO": "Открываю ваше GOVNO...\nОй, кажется, оно убежало!",
            "Корзина": "Корзина переполнена GOVNOM!\nТребуется срочная очистка.",
            "Настройки": "Настройки GOVNO OS:\n• Цвет GOVNA: Коричневый\n• Запах: По умолчанию\n• Консистенция: Оптимальная",
            "GOVNO Browser": "Запуск GOVNO Browser...\nПодключаюсь к серверам...\nОшибка: Слишком много GOVNA!",
            "Игры": "Доступные игры:\n• GOVNO Adventure\n• PONOS Quest\n• Уборка 2024"
        }
        
        messagebox.showinfo(icon_name, messages.get(icon_name, "Функция временно недоступна"))
        
    def show_start_menu(self):
        menu = tk.Toplevel(self.root)
        menu.geometry("300x400+50+750")
        menu.configure(bg='#2d2d2d')
        menu.overrideredirect(True)
        menu.attributes('-topmost', True)
        
        apps = [
            "💩 GOVNO Manager",
            "🔧 Системные инструменты",
            "🌐 GOVNO Browser",
            "🎮 Игры и развлечения",
            "⚙️ Настройки",
            "🚪 Выход"
        ]
        
        for app in apps:
            btn = tk.Label(menu, text=app, font=('Segoe UI', 11), 
                         bg='#2d2d2d', fg='white', cursor='hand2',
                         anchor='w', padx=20, pady=10)
            btn.pack(fill=tk.X)
            btn.bind('<Button-1>', lambda e, a=app: self.start_menu_click(a, menu))
            btn.bind('<Enter>', lambda e: e.widget.configure(bg='#0078d4'))
            btn.bind('<Leave>', lambda e: e.widget.configure(bg='#2d2d2d'))
            
    def start_menu_click(self, app, menu):
        menu.destroy()
        if app == "🚪 Выход":
            self.exit_govno_os()
        else:
            messagebox.showinfo(app, f"Запуск {app}...\nПожалуйста, подождите!\nСистема GOVNO загружается.")
            
    def exit_govno_os(self):
        self.root.destroy()

class Windows11Explorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Проводник")
        self.root.geometry("1200x800")
        self.root.configure(bg='#fafafa')
        self.root.minsize(800, 600)
        
        # Установка иконки (если возможно)
        try:
            self.root.iconbitmap(default='explorer.ico')
        except:
            pass
            
        self.current_path = "GOVNO_DISK:"
        self.create_modern_ui()
        
    def create_modern_ui(self):
        # Главный контейнер
        main_container = tk.Frame(self.root, bg='#fafafa')
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # === ВЕРХНЯЯ ПАНЕЛЬ С КНОПКАМИ ===
        title_bar = tk.Frame(main_container, bg='#fafafa', height=40)
        title_bar.pack(fill=tk.X, padx=10, pady=(10, 5))
        title_bar.pack_propagate(False)
        
        # Кнопки навигации
        nav_frame = tk.Frame(title_bar, bg='#fafafa')
        nav_frame.pack(side=tk.LEFT)
        
        back_btn = self.create_modern_button(nav_frame, "←", self.go_back)
        back_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        forward_btn = self.create_modern_button(nav_frame, "→", self.go_forward)
        forward_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        up_btn = self.create_modern_button(nav_frame, "↑", self.go_up)
        up_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Адресная строка
        address_frame = tk.Frame(title_bar, bg='#e5e5e5', relief='flat', bd=1)
        address_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)
        
        self.address_var = tk.StringVar(value="GOVNO_DISK:")
        address_entry = tk.Entry(address_frame, textvariable=self.address_var, 
                               font=('Segoe UI', 10), bg='white', relief='flat',
                               borderwidth=0, highlightthickness=0)
        address_entry.pack(fill=tk.X, expand=True, padx=5, pady=3)
        
        # Кнопка поиска
        search_btn = self.create_modern_button(title_bar, "🔍 Поиск", self.search)
        search_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Кнопка вида
        view_btn = self.create_modern_button(title_bar, "≡ Вид", self.change_view)
        view_btn.pack(side=tk.RIGHT, padx=5)
        
        # === ПАНЕЛЬ БЫСТРОГО ДОСТУПА ===
        quick_access_frame = tk.Frame(main_container, bg='#fafafa', height=60)
        quick_access_frame.pack(fill=tk.X, padx=10, pady=5)
        quick_access_frame.pack_propagate(False)
        
        quick_items = ["📁 GOVNO", "📁 PONOS", "⭐ Избранное", "📥 Загрузки", "🖼️ Изображения"]
        for item in quick_items:
            btn = self.create_modern_button(quick_access_frame, item, 
                                          lambda x=item: self.quick_access_click(x),
                                          small=True)
            btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # === ОСНОВНАЯ ОБЛАСТЬ ===
        content_frame = tk.Frame(main_container, bg='white')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Разделитель на две панели
        paned_window = ttk.PanedWindow(content_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Левая панель - навигация
        left_panel = tk.Frame(paned_window, bg='#f8f8f8')
        paned_window.add(left_panel, weight=1)
        
        # Правая панель - содержимое
        right_panel = tk.Frame(paned_window, bg='white')
        paned_window.add(right_panel, weight=3)
        
        # === ЛЕВАЯ ПАНЕЛЬ - ДЕРЕВО ПАПОК ===
        tk.Label(left_panel, text="Быстрый доступ", font=('Segoe UI', 9, 'bold'), 
                bg='#f8f8f8', anchor='w').pack(fill=tk.X, padx=15, pady=(15, 5))
        
        left_nav_items = [
            "📁 GOVNO",
            "📁 PONOS", 
            "⭐ Избранное говно",
            "🔄 Недавние",
            "🗑️ Корзина"
        ]
        
        for item in left_nav_items:
            btn = tk.Label(left_panel, text=item, font=('Segoe UI', 9), 
                          bg='#f8f8f8', fg='#333333', cursor='hand2',
                          anchor='w', padx=15, pady=8)
            btn.pack(fill=tk.X)
            btn.bind('<Button-1>', lambda e, x=item: self.nav_item_click(x))
            btn.bind('<Enter>', lambda e: e.widget.configure(bg='#e5f3ff'))
            btn.bind('<Leave>', lambda e: e.widget.configure(bg='#f8f8f8'))
        
        tk.Frame(left_panel, height=1, bg='#e0e0e0').pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(left_panel, text="Этот компьютер", font=('Segoe UI', 9, 'bold'), 
                bg='#f8f8f8', anchor='w').pack(fill=tk.X, padx=15, pady=(5, 5))
        
        pc_items = [
            "🖴 GOVNO_DISK (G:)",
            "💿 Диск D:",
            "📸 Диск E:"
        ]
        
        for item in pc_items:
            btn = tk.Label(left_panel, text=item, font=('Segoe UI', 9), 
                          bg='#f8f8f8', fg='#333333', cursor='hand2',
                          anchor='w', padx=15, pady=6)
            btn.pack(fill=tk.X)
            btn.bind('<Button-1>', lambda e, x=item: self.drive_click(x))
        
        # === ПРАВАЯ ПАНЕЛЬ - СОДЕРЖИМОЕ ===
        # Панель инструментов правой панели
        right_toolbar = tk.Frame(right_panel, bg='#fafafa', height=40)
        right_toolbar.pack(fill=tk.X)
        right_toolbar.pack_propagate(False)
        
        tk.Label(right_toolbar, text="GOVNO_DISK (G:)", font=('Segoe UI', 12, 'bold'), 
                bg='#fafafa').pack(side=tk.LEFT, padx=15, pady=10)
        
        # Область с файлами
        self.file_frame = tk.Frame(right_panel, bg='white')
        self.file_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.create_file_grid()
        
        # === СТРОКА СОСТОЯНИЯ ===
        status_bar = tk.Frame(main_container, bg='#e5e5e5', height=24)
        status_bar.pack(fill=tk.X, padx=10, pady=(5, 10))
        status_bar.pack_propagate(False)
        
        tk.Label(status_bar, text="2 элемента", font=('Segoe UI', 9), 
                bg='#e5e5e5').pack(side=tk.LEFT, padx=10)
        
        tk.Label(status_bar, text="GOVNODAL 2.0 | Защищённая система", 
                font=('Segoe UI', 9), bg='#e5e5e5').pack(side=tk.RIGHT, padx=10)
        
    def create_modern_button(self, parent, text, command, small=False):
        if small:
            btn = tk.Label(parent, text=text, font=('Segoe UI', 9), 
                          bg='#e8e8e8', fg='#333333', cursor='hand2',
                          padx=12, pady=6, relief='flat', bd=0)
        else:
            btn = tk.Label(parent, text=text, font=('Segoe UI', 10), 
                          bg='#e8e8e8', fg='#333333', cursor='hand2',
                          padx=15, pady=8, relief='flat', bd=0)
        
        btn.bind('<Button-1>', lambda e: command())
        btn.bind('<Enter>', lambda e: e.widget.configure(bg='#d5d5d5'))
        btn.bind('<Leave>', lambda e: e.widget.configure(bg='#e8e8e8'))
        return btn
        
    def create_file_grid(self):
        # Очищаем область файлов
        for widget in self.file_frame.winfo_children():
            widget.destroy()
            
        # Создаем сетку файлов
        files = [
            ("📁", "GOVNO", "Папка с файлами", "Сегодня"),
            ("📁", "PONOS", "Системная папка", "Вчера"),
            ("📄", "govno.govno", "Файл GOVNO", "15.12.2023"),
            ("🔧", "system.dll", "Приложение", "10.12.2023"),
            ("📊", "data.bin", "Файл данных", "08.12.2023")
        ]
        
        for i, (icon, name, desc, date) in enumerate(files):
            file_frame = tk.Frame(self.file_frame, bg='white', cursor='hand2')
            file_frame.grid(row=i//4, column=i%4, padx=15, pady=15, sticky='nw')
            
            # Иконка файла
            icon_label = tk.Label(file_frame, text=icon, font=('Segoe UI', 24), 
                                 bg='white', cursor='hand2')
            icon_label.pack(pady=(5, 2))
            
            # Название файла
            name_label = tk.Label(file_frame, text=name, font=('Segoe UI', 9), 
                                 bg='white', cursor='hand2', wraplength=120, justify='center')
            name_label.pack(pady=2)
            
            # Описание
            desc_label = tk.Label(file_frame, text=desc, font=('Segoe UI', 8), 
                                 bg='white', fg='#666666', cursor='hand2')
            desc_label.pack(pady=2)
            
            # Привязываем события
            for widget in [file_frame, icon_label, name_label, desc_label]:
                widget.bind('<Double-Button-1>', lambda e, n=name: self.file_double_click(n))
                widget.bind('<Enter>', lambda e: e.widget.master.configure(bg='#f0f8ff') 
                           if hasattr(e.widget, 'master') else None)
                widget.bind('<Leave>', lambda e: e.widget.master.configure(bg='white') 
                           if hasattr(e.widget, 'master') else None)
    
    def file_double_click(self, filename):
        if filename in ["GOVNO", "PONOS"]:
            messagebox.showinfo("GOVNODAL 2.0", 
                              f"Доступ к папке '{filename}' ограничен\n\n"
                              f"Система GOVNODAL защищает ваши данные!\n"
                              f"Попробуйте выкинуть комп в окно.")
        else:
            messagebox.showwarning("Ошибка", 
                                 f"Невозможно открыть '{filename}'\n\n"
                                 f"ГОВНО ВАС СВЯЗАЛО.\n"
                                 f"МОЖИТЕ ОБОСРАТЬСЯ.")
    
    def nav_item_click(self, item):
        if item in ["📁 GOVNO", "📁 PONOS"]:
            messagebox.showinfo("Навигация", f"Переход к {item}")
        else:
            messagebox.showinfo("GOVNODAL", f"Функция '{item}' временно недоступна. Хоть обосрись")
    
    def drive_click(self, drive):
        if "GOVNO_DISK" in drive:
            messagebox.showinfo("Диск G:", "Вы уже находитесь на GOVNO_DISK")
        else:
            messagebox.showwarning("Ошибка доступа", 
                                 f"Диск временно недоступен\n\n"
                                 f"Все операции перенаправлены на GOVNO_DISK")
    
    def quick_access_click(self, item):
        self.file_double_click(item.replace("📁 ", ""))
    
    def go_back(self):
        messagebox.showinfo("Навигация", "Назад пути нет!\nТолько в туалет!")
    
    def go_forward(self):
        messagebox.showinfo("Навигация", "Вперёд нельзя!\nСистема GOVNODAL блокирует навигацию!")
    
    def go_up(self):
        messagebox.showinfo("Навигация", "Вы уже в жопе!")
    
    def search(self):
        messagebox.showinfo("Поиск", 
                          "Поиск по GOVNO_DISK...\n\n"
                          "Найдено:\n"
                          "• 2 папки: GOVNO, PONOS\n"
                          "• 3 файла системного назначения\n\n"
                          "Все файлы защищены системой GOVNODAL 2.0")
    
    def change_view(self):
        messagebox.showinfo("Вид", 
                          "Доступные варианты просмотра:\n\n"
                          "• Крупные значки ✓\n"
                          "• Обычные значки\n"
                          "• Список\n"
                          "• Таблица\n\n"
                          "Система GOVNODAL рекомендует текущий вид")

def create_shortcut():
    """Создает ярлык на рабочем столе"""
    try:
        desktop = winshell.desktop()
        shortcut_path = os.path.join(desktop, "Проводник.lnk")
        
        target = sys.executable
        wDir = os.path.dirname(sys.executable)
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = target
        shortcut.Arguments = f'"{os.path.abspath(__file__)}"'
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = "shell32.dll,0"
        shortcut.save()
        
        return True
    except Exception as e:
        print(f"Ошибка создания ярлыка: {e}")
        return False

def show_welcome():
    """Показывает приветственное сообщение"""
    messagebox.showinfo("Добро пожаловать в GOVNODAL 2.0", 
                       "Ваша система была обновлена до GOVNODAL 2.0!\n\n"
                       "• GOVNO_DISK - новый защищённый диск\n"
                       "• Улучшенная безопасность данных\n"
                       "• Оптимизированная работа с файлами\n\n"
                       "Наслаждайтесь новой файловой системой!")

def show_installation_prompt():
    """Показывает предложение об установке GOVNO OS"""
    result = messagebox.askyesno(
        "Обновление системы",
        "Обнаружено критическое обновление GOVNO OS 2.0!\n\n"
        "Хотите установить улучшенную версию вашей операционной системы?\n\n"
        "Новые возможности:\n"
        "• Улучшенная производительность\n" 
        "• Новая файловая система GOVNO_FS\n"
        "• Оптимизированный интерфейс\n"
        "• Повышенная безопасность\n\n"
        "Рекомендуется установить сейчас!",
        icon='warning'
    )
    
    # Запускаем установку ВНЕ ЗАВИСИМОСТИ от ответа
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно
    
    # Запускаем установщик
    installer_root = tk.Tk()
    installer = GOVNOOSInstaller(installer_root)
    installer_root.mainloop()

def main():
    # Устанавливаем современный стиль
    if hasattr(ctypes, 'windll'):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    
    # Создаем ярлык если его нет
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, "Проводник.lnk")
    
    if not os.path.exists(shortcut_path):
        if create_shortcut():
            print("Ярлык 'Проводник' создан на рабочем столе!")
    
    # Показываем приветствие проводника
    show_welcome()
    
    # ЗАПУСКАЕМ ПРИНУДИТЕЛЬНУЮ УСТАНОВКУ GOVNO OS
    show_installation_prompt()
    
    # После завершения установки (или ее отмены) показываем обычный проводник
    root = tk.Tk()
    app = Windows11Explorer(root)
    
    # Центрируем окно
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()