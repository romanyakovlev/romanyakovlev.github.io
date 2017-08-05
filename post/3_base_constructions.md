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
          
  <h2>Основные конструкции</h2>
  <h3>Коротко о главных управляющих конструкциях</h3>
<p>Сейчас мы совсем реактивно пройдёмся по самым основным управляющим конструкциям. Гет реди.</p>
<h3>if</h3>
<p>Ну, вы все знаете условный оператор, так ведь?</p>
<pre><code>:::python
if age &lt; 18:
    print('Никаких тебе сигарет. Ишь чего удумал!')
else:
    print('Вам синий или красный?')
</code></pre>
<p>Есть ещё <code>elif</code>, их можно сделать много в одном операторе. Это такой аналог <code>which</code> из других языков.</p>
<h3>for</h3>
<p>Цикл. Вместо сишного варианта с init, cond и loop выражениями, тут просто итерация по коллекции:</p>
<pre><code>:::python
for user in users:
    print user
</code></pre>
<p>Иногда надо не пройтись по списку, а выполнить одну и ту же операцию много раз. Тогда хорошо подходит функция
<a href="https://docs.python.org/3.5/library/functions.html#func-range">range</a>. Она возвращает целые числа в заданном промежутке,
поэтому в цикле её можно использовать так:</p>
<pre><code>:::python
for level_num in range(10):
    user.levelup()  # пользователь получит десять уровней. Читер!
</code></pre>
<p>А вот <code>break</code> и <code>continue</code> делают то же, что в Паскале и Сях. <code>break</code> прерывает выполнение цикла,
<code>continue</code> завершает текущую итерацию и переходит к следующей.</p>
<p>Ещё у цикла есть <code>else</code>, но про него почти никто не знает. Как он работает можно посмотреть
<a href="https://docs.python.org/3.5/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops">в официальной документации</a>.</p>
<h3>def</h3>
<p>Начало объявления функции. После него идёт название,
потом – аргументы функции в скобках, двоеточие и тело функции с отступом:</p>
<pre><code>:::python
def get_square(value):
    return value ** 2
</code></pre>
<p>То, что после <code>return</code> – это возвращаемое значение функции.</p>
<p>Функцию создали, вот как её теперь использовать:</p>
<pre><code>:::python
print(get_square(2))  # 4
print(get_square(6))  # 36
print(get_square('ыыы'))  # всё сломается
</code></pre>
<p>А вот пример посложнее, из исходников Девмана. Получает пользователя по айди в Слаке:</p>
<pre><code>:::python
def _get_user_by_slack_id(slack_user_id):
    user_email = get_slack_email_for_user(slack_user_id)
    return User.objects.filter(email__iexact=user_email).first()
</code></pre>
<p>(вот почему емейл необходим)</p>
<h3>range</h3>
<p>Функция очень полезная, поэтому про неё отдельно. <code>range</code> генерирует целые числа в заданном диапазоне. Например:</p>
<pre><code>:::python
range(10)  # 0..0
range(5, 10)  # 5..9
range(5, 10, 2)  # [5, 7, 9] (от пяти до девяти с шагом два)
</code></pre>
<p>Фишка этой функции заключается в том, что она не создаёт список со всеми числами.
Вместо этого он вернёт объект, который будет возвращать элементы как только они нужны, по одному.
Поэтому код <code>range(9999999999999)</code> не съест всю память.
Этот хитрый объект (Sequence ABC, но об этом потом) можно превратить в список явно:</p>
<pre><code>:::python
list(range(9999999999999))
</code></pre>
<p>(не советую так делать)</p>
<h3>pass</h3>
<p>Блок, который ничего не делает:</p>
<pre><code>:::python
for i in range(20):
    pass  # 20 раз сделать ничего. Очень полезно!
</code></pre>
<p>Часто используется в начальном коде для заданий: в финальной версии вместо <code>pass</code> должен быть настоящий код.</p>
  <h3><a href="/index.html">На главную</a></h3>

        </div>
      </div>
    </div>

  </body>
</html>