<h1 align="center">Словестная игра в <a>Города</a></h1>
<h3 align="left">Описание процесса игры</h3>
<body style="font-size: 16px;">
<p style="text-indent: 30px;">Города — игра для одного человек и ИИ, в которой участник и компьютер в свою 
очередь называют реально существующий город России, название которого 
начинается на ту букву, которой оканчивается название предыдущего города. Проигрывает тот,
кто не может назвать нового города.</p> 
<h3>Исключения</h3>
<ul>
  <li>Город не может начинаться с букв: "Ъ", "Ь", "Ы", "Й".</li>
<i><span style="font-size: 13px;">Условие с "Й" добавлено для того, чтобы игра не завершилось быстро. Из-за существования 
в России всего 1 города на "Й".</span></i>
  <li>Города не могут повторяться</li>
  <li>Названия городов не могут быть вымышленными</li>
</ul>
<h3>Использование (распаковка) проекта</h3>
<p style="text-indent: 30px;">Загружаем папку <code>cities_game</code>. Распаковываем командой <code>docker-compose up</code>.
Теперь приложение доступно из docker контейнера.</p>
<h3>Структура проекта</h3>
<ul>
<li><code>backend</code></li>
    <ul>
    <li><code>cities.txt</code></li>
    <li><code>Dockerfile</code></li>
    <li><code>main.py</code></li>
    <li><code>models.py</code></li>
    <li><code>requirements.txt</code></li>
    </ul>
<li><code>frontend</code></li>
    <ul>
    <li><code>Dockerfile</code></li>
    <li><code>client.py</code></li>
    <li><code>requirements.txt</code></li>
    </ul>
<li><code>docker-compose.yml</code></li>
<li><code>README.md</code></li>
</ul>
<p style="text-indent: 30px;">Файл <code>cities.txt</code> выступает некой базой данных, в котором содержится список 
всех известных город в России.</p>
<p style="text-indent: 30px;"><code>client.py</code> - файл с вводом и выводом данных на фреймворке Streamlit. С помощью данного
файла запускается видимая пользователю часть проекта.</p>
<p style="text-indent: 30px;"><code>main.py</code> - простейший файл FastApi, состоящий из одного запроса <code>post</code>.</p>
<p style="text-indent: 30px;"><code>models.py</code> - основной файл, "тело" нашего приложения, в котором прописаны все его функции.</p>
</body>
