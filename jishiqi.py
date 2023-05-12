import time
import tkinter as tk

def start_timer(start_time, time_pool):
    def update_time():
        nonlocal start_time, time_pool
        current_time = time.time() - start_time
        time_label.config(text="当前时间：{:.1f}".format(current_time))
        
        if time_pool > 0:
            time_pool -= 1
            root.after(1000, update_time)
        else:
            time_label.config(text="倒计时结束！")

    def start_count_up():
        nonlocal start_time, time_pool
        start_time = time.time() - time_pool
        update_time()

    def start_count_down():
        nonlocal start_time, time_pool
        start_time = time.time()
        update_time()

    root = tk.Tk()
    root.title("计时器")
    root.geometry("300x200")

    time_label = tk.Label(root, text="当前时间：0.0", font=("Arial", 16))
    time_label.pack(pady=20)

    count_up_btn = tk.Button(root, text="正计时", command=start_count_up)
    count_up_btn.pack(pady=10)

    count_down_btn = tk.Button(root, text="倒计时", command=start_count_down)
    count_down_btn.pack(pady=10)

    root.mainloop()

start_time = 0
time_pool = 0

start_timer(start_time, time_pool)
