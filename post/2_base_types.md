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
          
  <h2>Основные типы данных</h2>
  <h3>О типах данных по-быстрому</h3>
<p>Цель этого подмодуля – по-быстрому рассказать о основных типах данных и дать их потрогать.
Позже мы познакомимся с типами куда обстоятельнее.</p>
<h3>Целые и вещественные числа</h3>
<p>Числа – и в Африке числа. С ними можно производить арифметические действия. Всё просто:</p>
<pre><code>:::python
2 + 2  # 4
3 + 2.5  # 5.5
6 / 2  # 3
2 ** 3  # 8
</code></pre>
<p>Решётка – это знак комментария в Питоне,
а в этом туториале результат работы команды указан на той же строчке за комментарием.</p>
<p>[q Исправьте ошибку. Программа должна выводить число <code>value</code> в кубе.]</p>
<h1>===</h1>
<p>===
power medium
===
value = 5
print(value * 3)
===
value = 5
print(value ** 3)
===</p>
<h3>Строки</h3>
<p>Помимо чисел в Питоне есть строки с богатым набором встроенных функций. С ними просто и удобно работать:</p>
<pre><code>:::python
'hello'  # строковая константа
"hello"  # тип кавычек не имеет значения
hello[1]  # 'e'
'hello' + ' ' + 'world'  # 'hello world'
'blah ' * 3  # 'blah blah blah '
</code></pre>
<p>У них много встроенных функций:</p>
<pre><code>:::python
'hello  '.strip()  # 'hello'
'hello world'.upper()  # 'HELLO WORLD'
len('hello')  # 5
'wor' in 'hello world'  # True (входит ли "wor" в строку "hello world")
'hello world'.startswith('hel')  # True (начинается ли  "hello world" c "hel")
</code></pre>
<p>Ещё можно превращать строку в список, список в строку,
получать подстроку и по-разному форматировать значения, но об этом позже.</p>
<h3>Список</h3>
<p>Список – последовательность элементов. Ограничения на длину нет.
Элементы могут быть разных типов, даже другими списками. Выглядит он так:</p>
<pre><code>:::python
[1, 2, 3]  # в квадратных скобках, элементы через запятую
digits = [4, 5, 6]  # переменная, в которой живёт список
digits[0]  # 4 (нумерация с нуля)
digits[1] = 22  # теперь в списке digits на втором месте стоит 22
digits.append(8)  # а теперь в конец добавилась восьмёрка
</code></pre>
<p>Из списка надо часто получить подсписок: несколько первых элементов, последних, что-то из середины.
Это называется срезами и позволяет делать много чего. Вот самые простые срезы:</p>
<pre><code>:::python
squares = [1, 4, 9, 16, 25, 36, 49]
squares[1:3]  # [4, 9] (элементы со второго по третий)
squares[:4]  # [1, 4, 9, 16] (элементы с начала до четвёртого)
squares[4:]  # [25, 36, 49] (элементы с пятого до конца)
squares[1:6:2]  # [4, 16, 36] (элементы со второго до шестого с шагом два)
</code></pre>
  <h3><a href="/index.html">На главную</a></h3>

        </div>
      </div>
    </div>

  </body>
</html>