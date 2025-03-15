<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
<body>

<section>
    <h2>Описание</h2>
    <p>Этот скрипт предназначен для проведения <strong>DDoS-атаки</strong> на выбранный IP-адрес с использованием UDP-пакетов. Программа позволяет атаковать конкретный порт или диапазон портов на целевой машине с заданным количеством потоков и длительностью атаки. Этот код является демонстрационным и образовательным, и его не следует использовать в любых незаконных или вредоносных целях.</p>

    <h3>Основные функции:</h3>
    <ul>
        <li><strong>Выбор целевого IP</strong>: Пользователь вводит IP-адрес, на который будет направлена атака.</li>
        <li><strong>Выбор порта/диапазона портов</strong>: Пользователь может указать конкретный порт или диапазон портов для атаки.</li>
        <li><strong>Указание продолжительности атаки</strong>: Атака будет продолжаться заданное количество времени.</li>
        <li><strong>Количество потоков</strong>: Можно указать количество параллельных потоков для ускорения атаки.</li>
        <li><strong>Простой интерфейс</strong>: Ввод данных через консоль с валидацией и обработкой ошибок.</li>
        <li><strong>Анимация загрузки</strong>: Визуализация начала атаки с анимацией.</li>
        <li><strong>Обработка ошибок</strong>: Программа безопасно обрабатывает прерывание атаки пользователем и возможные исключения.</li>
    </ul>
</section>

<section>
    <h2>Требования</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Модуль <code>multiprocessing</code> для многозадачности.</li>
        <li>Модуль <code>socket</code> для работы с сетевыми запросами.</li>
        <li>Модуль <code>random</code> для генерации случайных данных.</li>
    </ul>
</section>

<section>
    <h2>Инструкция по использованию</h2>
    <p>Следуйте этим шагам для использования скрипта:</p>
    <ol>
        <li>Склонируйте репозиторий:
            <pre><code>git clone https://github.com/yourusername/ddos-attack-simulator.git
cd ddos-attack-simulator</code></pre>
        </li>
        <li>Убедитесь, что у вас установлен Python 3 и все необходимые модули.</li>
        <li>Запустите скрипт:
            <pre><code>python3 attack_script.py</code></pre>
        </li>
        <li>Следуйте инструкциям в консоли для ввода:
            <ul>
                <li><strong>IP-адрес</strong>: Введите целевой IP.</li>
                <li><strong>Порт/диапазон портов</strong>: Введите номер порта или диапазон (например, <code>1-80</code>).</li>
                <li><strong>Длительность атаки</strong>: Введите продолжительность атаки в секундах.</li>
                <li><strong>Количество потоков</strong>: Введите количество параллельных потоков (от 1 до 100).</li>
            </ul>
        </li>
        <li>Программа начнёт атаку, и вы увидите информацию о количестве отправленных пакетов.</li>
    </ol>
</section>

<section>
    <h2>Пример вывода</h2>
    <pre><code>Attack started: 2025-03-15 10:00:00
  BBBBB   EEEEE  TTTTTТТ   AAAA      DDDD    DDDD    OOO   SSSSS
  B    B  E         T     A    A     D   D   D   D   O   O  S
  BBBBB   EEEE      T     AAAAAA     D   D   D   D   O   O  SSSS
  B    B  E         T     A    A     D   D   D   D   O   O     S
  BBBBB   EEEEE     T     A    A     DDDD    DDDD    OOO   SSSSS

Author   : Adresatov
TEAM     : Collapse

Enter target IP address: 192.168.1.1
Enter port or port range (e.g., 1 or 1-80): 80
Enter attack duration in seconds: 60
Enter the number of threads (1-100): 10

Starting attack... | Attack initiated!
Sent 1000 packets to 192.168.1.1 via port 80
Sent 2000 packets to 192.168.1.1 via port 80
...
Attack finished!</code></pre>
</section>

<section>
    <h2>Пояснение к коду</h2>
    <p>1. <strong>Переменные и настройки</strong>: Код автоматически определяет команду для очистки экрана в зависимости от операционной системы (Windows или Linux/Mac).</p>
    <p>2. <strong>Ввод данных</strong>: Программа запрашивает у пользователя IP-адрес, порты, длительность атаки и количество потоков.</p>
    <p>3. <strong>Анимация загрузки</strong>: Используется цикл с анимацией для визуального представления начала атаки.</p>
    <p>4. <strong>Основная логика атаки</strong>: В многозадачности используется модуль <code>multiprocessing</code>, чтобы распараллелить процесс атаки и ускорить выполнение.</p>
</section>

<section>
    <h2>Примечания по безопасности</h2>
    <div class="note">
        <p class="important">Убедитесь, что вы используете этот скрипт только в целях тестирования и обучения.</p>
        <p><strong>Проведение DDoS-атак против несанкционированных систем является уголовно наказуемым деянием.</strong> Код предоставляется исключительно в образовательных целях и для тестирования на своих собственных системах.</p>
    </div>
</section>

</body>
</html>
