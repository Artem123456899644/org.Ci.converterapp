[app]

# Имя приложения (только символы ASCII)
title = Converter

# Пакет ID вашего приложения (должен быть уникальным для каждого приложения)
package.name = convertapp

# Версия приложения
package.version = 0.3

# Идентификатор приложения в формате Java package
package.domain = org.ci

# Имя иконки приложения (в папке data/logo/icon.png)
source.icon = data/logo/icon.png

# Имя файла запуска приложения
source.include_exts = py,png,jpg,kv,ttf

# Зависимости на Python
requirements = kivy,android, python3

# Версия Python
python.version = 3.8

# Компилировать Cython код перед сборкой
source.include_exts = py,png,jpg,kv,ttf,pyx

# Компилировать Cython код в отдельные модули
cython.max_cache = 0

# Добавить параметры сборки дополнительных расширений
android.permissions = INTERNET
#android.api = 29
#android.ndk = 21.1.6352462
android.arch = armeabi-v7a
#android.gradle_dependencies = 'com.android.support:appcompat-v7:28.0.0'

