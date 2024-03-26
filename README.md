# рабочая директория проекта /var/www/myproject/
# установим пакеты
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
# настройка виртуальной среды
sudo apt install python3-venv
# перейдем в директорию проекта и запустим виртуальную среду
python3 -m venv myprojectenv
# активируем виртуальную среду
source myprojectenv/bin/activate
# Обновим pip:
pip install -U pip
# Следом загрузим Flask и Gunicorn:
pip install gunicorn flask
# установим инструменты сборки модуля flask_mysqldb
apt-get install pkg-config build-essential libmysqlclient-dev
# и сам модуль
pip install flask_mysqldb
