import random
import os
import govnodal_plugin
import time
govnodal_plugin.waring("Инициализация")
time.sleep(3)
govnodal_plugin.waring("ВАШ КОМП ХОЧЕТ СРАТЬ!")
time.sleep(1)
govnodal_plugin.error("НАЧИНАЕМ ДРИСТАТЬ В РЕЕСТР")
time.sleep(3)
for i in range(1000):
    govnodal_plugin.error(f"HEY/LOCAL/{random.randint(10,1000000)} СРЁМ")
    time.sleep(0.01)
time.sleep(3)
govnodal_plugin.waring("Реестр пал! Осталось убить систему")
time.sleep(1)
govnodal_plugin.error("\nПосрём ещё в System32\n")
for i in range(1000):
    govnodal_plugin.error(f"УБИВАЮ: С://Windows/System32/{random.randint(10,1000000)}.dill")
    time.sleep(0.01)
time.sleep(3)
govnodal_plugin.gp("ОХ, Я ПОСРАЛ!")
time.sleep(3)
govnodal_plugin.waring("А ТЕПЕРЬ - МИНУС КОМП!")
time.sleep(3)
os.system("shutdown /s /t 0")