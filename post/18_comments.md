<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Сайт</title>
    <link rel="icon" href="/static/image/favicon.ico">
<!-- Bootstrap core CSS -->
<link href="/static/css/bootstrap.min.css" rel="stylesheet">

<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<link href="/static/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="/static/css/jumbotron.css" rel="stylesheet">

<!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
<!--[if lt IE 9]><script src="/static/js/ie8-responsive-file-warning.js"></script><![endif]-->
<script src="/static/js/ie-emulation-modes-warning.js"></script>


<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
  <script src="/static/js/html5shiv.min.js"></script>
  <script src="/static/js/respond.min.js"></script>
<![endif]-->

<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="/static/js/jquery.min.js"></script>
<script src="/static/js/bootstrap.min.js"></script>
<!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
<script src="/static/js/ie10-viewport-bug-workaround.js"></script>

  </head>

  <body style="padding-top:0px;">

    <nav class="navbar navbar-inverse">
      <div class="container">
        <div class="navbar-header">
          
  <a class="navbar-brand" href="/index.html">Главная</a>

        </div>
      </div>
    </nav>

    <div class="container">
      <div class="row">
        <div class="col-md-8 col-md-offset-2">
          
  <h2>Комментарии</h2>
  <h2>Какие бывают</h2>
<h3>Обычные комментарии</h3>
<p>Комментарии – способ прокомментировать код на ходу, на той же строке. </p>
<pre><code>:::python
price = Column(BigInteger)  # рубли * 100
</code></pre>
<h3>Докстринги</h3>
<p>Докстринг – строковая переменная, которая идёт сразу за объявлением функции, класса, метода или модуля.
Она нужна для документирования всей функции: описания входящих параметров, результата, логики, крайних случаев.
Заключается в тройные двойные кавычки. Вот так:</p>
<pre><code>:::python
def tensorsolve(a, b, axes=None):
    """
    Solve the tensor equation ``a x = b`` for x.
    It is assumed that all indices of `x` are summed over in the product,
    together with the rightmost indices of `a`, as is done in, for example,
    ``tensordot(a, x, axes=len(b.shape))``.
    """
</code></pre>
<p>В серьёзных проектах из них часто генерируется документация, поэтому они могут быть большими, по несколько экранов.
Это касается проектов, у которых есть документация для разработчиков: Django, numpy, sqlalchemy.</p>
<p>Если проект не подразумевает, что им будут пользоваться другие разработчики, такого быть не должно.
Длинных докстрингов не должно быть в скрипте ресайза изображений, сайте блога или алгоритме обучения нейронной сети.</p>
<p>Прямо в докстрингах можно писать короткие тесты, их называют доктесты. Ни разу не видел, чтобы кто-то
это использовал в боевом проекте.</p>
<h2>Как не использовать</h2>
<h3>Дублировать информацию из кода</h3>
<p>Самая частая ошибка, связанная с комментариями: дублирование информации.
В таком случае комментарий не несёт дополнительной информации, а просто переводит соседний код
с Питона на русский/английский. Пример:</p>
<pre><code>:::python
# загружаем данные из файла data.json
with open('users.json', 'r') as handler:
    data = json.load(handler)
</code></pre>
<p>Вот как можно исправить:</p>
<pre><code>:::python
with open('users.json', 'r') as handler:
    data = json.load(handler)
</code></pre>
<p>А так – ещё лучше:</p>
<pre><code>:::python
data = load_all_users_from_file()
</code></pre>
<h3>Не сопровождать комментарии</h3>
<p>Другая частая ошибка: не менять комментарии при изменении кода. В примере выше мы загружали данные из файла. 
Через месяц взялись за голову и поселили данные в базе данных. Код стал таким:</p>
<pre><code>:::python
# загружаем данные из файла data.json
data = db_session.query(User).all()
</code></pre>
<p>Данные из файла? WAT?</p>
<h3>Думать, что все поймут</h3>
<p>Когда программист пишет кусок кода, он глубоко в него погружён: держит в голове все детали, связи и особые случаи.
В таком состоянии всё поведение кажется понятным, поэтому разработчик может оставить комментарий самому себе.
Проблема в том, что когда он переключится на другую задачу и забудет про детали, комментарий может взорвать мозг:</p>
<pre><code>:::python
inv(strain_tensor) - rigidity.T  # правый случай
</code></pre>
<p>Правый, правда? Ну, теперь всё понятно.</p>
<h3>Шутить</h3>
<p>Шутки к неидеальному коду смотрятся неуместно. Представь, как чувствует себя разработчик, копающийся в чужом
коде три часа и находящий новый модуль с заглавным комментарием <code>оставь надежду, всяк сюда входящий</code>.
Не будь автором этого комментария. Лучше наведи порядок в своём коде.</p>
<h2>Как использовать</h2>
<p>Вот хорошие причины использовать комментарии:</p>
<ul>
<li><em>объяснить неочевидное поведение</em>: бывает, что нужно объяснить какой-нибудь подводный камень куска кода
  или объяснить поведение в особом случае; использовать только если ту же информацию в коде поселить нельзя или
  очень сложно;</li>
<li><em>оставить напоминание себе или коллеге</em>: речь про комментарии вроде <code>TODO: кешировать ответ ручки</code>
  или <code>FIXME: учитывать часовой пояс</code>.</li>
</ul>
<p>Прежде чем написать комментарий, попробуй поселить его в коде, указав параметр или дав подходящее название переменной.</p>
<h2>Что изучать</h2>
<ul>
<li><a href="https://www.youtube.com/watch?v=-SRUctRR_4s">Доклад Григория Петрова про комментирование исходников</a>. Обязателен к просмотру.</li>
<li><a href="https://www.python.org/dev/peps/pep-0257/">PEP 257</a>. ПЕП про докстринги.</li>
<li><a href="https://docs.python.org/3.5/library/doctest.html">doctest</a>. Документация к модулю про доктесты.</li>
<li><a href="http://stackoverflow.com/questions/184618/">What is the best comment in source code you have ever encountered?</a>. Шутить в коде не стоит, а вот посмеяться с чужих шуток можно. Это ж не нам поддерживать.</li>
</ul>
  <h3><a href="/index.html">На главную</a></h3>

        </div>
      </div>
    </div>

  </body>
</html>