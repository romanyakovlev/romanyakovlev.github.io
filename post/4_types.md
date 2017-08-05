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
          
  <h2>Типы данных</h2>
  <h3>Числа</h3>
<p>В самом Питоне есть целые, вещественные, и комплексные числа. В стандартной библиотеке есть ещё рациональные и
фиксированной точности.</p>
<p>У целых чисел нет подводных камней: у них нет ограничения по размеру, поддерживают стандартные арифметические действия
и всякое такое.</p>
<p>У вещественных есть подвох: они внутри представлены как тип double в С++. Это значит, что хранятся они как два числа:
мантисса и экспонента. Это удобно, но иногда из-за ошибок округления и накапливаемых погрешностей происходят ужасные вещи.
Чтобы знать, что и как может сломаться, надо прочитать
<a href="https://docs.python.org/3.5/tutorial/floatingpoint.html">статью про ограничение вещественных числах в документации</a>
(<em>мастрид</em>).</p>
<p>Частный, но важный случай: деньги нельзя хранить как вещественное число, только как целое или с фиксированной точностью.
Это кажется очевидным, но многие так делают (некоторые даже в бою). Их всех потом увольняют. Едва ли это совпадение.</p>
<p><a href="https://docs.python.org/3.5/library/stdtypes.html#numeric-types-int-float-complex">Официальная заметка про численные типы</a>
короткая и понятная.</p>
<h3>Строки</h3>
<p>Со строками в третьем Питоне всё просто: они Юникодные.</p>
<p>Это значит, что всё сделано очень удобно, но чтобы этим всем удобно пользоваться, надо знать, что такое Юникод, кодировки,
байты, вот это всё. Об этом можно узнать, например, из <a href="https://www.youtube.com/watch?v=sgHbC6udIqc">классного доклада про Юникод в Питоне</a>.</p>
<p>Ещё строки можно форматировать, причём несколькими способами. Вот один из них:</p>
<pre><code>:::python
name = 'Пётр'
height = 1.865
print('Привет, %s! Твой рост – %.2f м.' % (name, height))
# Привет, Пётр! Твой рост – 1.86 м.
</code></pre>
<p>Заметь, что <code>%s</code> значит "вывести строку как есть", а <code>%.2f</code> значит "вывести вещественное число 
с точностью до третьего знака". На самом деле, есть целый подъязык этого форматирования. Почитай 
<a href="https://docs.python.org/3.1/library/string.html#format-specification-mini-language">про него в документации</a>
и <a href="https://pyformat.info/">более подробную статью</a>.</p>
<p>И главное: никогда не используй сложение строк для форматирования. Это плохо читается, долго работает и занимает
много места.</p>
<h3>Списки</h3>
<p>Всё необходимое для начала работы со списками, есть в разделе <a href="http://devman.org/encyclopedia/python_basics/python_basics_base_types/">"Основные типы данных"</a>.</p>
<p>Тут давайте немного поговорим о list comprehension (по-русски они зовутся списковыми выражениями, но я ни разу не слышал,
чтобы кто-то так говорил).</p>
<p>Часто бывает надо взять исходный список и сформировать из него новый, применив к каждому элементу исходного
какое-то преобразование и как-то отфильтровав. Например, так:</p>
<pre><code>:::python
values = [1, 2, 3, 4, 5]
new_values = []
for value in values:
    if value % 2:
        new_values.append(value ** 2)
</code></pre>
<p>В результате в <code>new_values</code> будут только квадраты чётных чисел из исходного списка.</p>
<p>Эта операция настолько частая, что для неё есть отдельная конструкция – list comprehension. Выглядит она так:</p>
<pre><code>:::python
values = [1, 2, 3, 4, 5]
new_values = [value ** 2 for value in values if value % 2]
</code></pre>
<p>Это та же конструкция, что и в предыдущем примере, просто записанная очень компактно: посредине тот же цикл,
слева – что добавлять в новый список, а справа - фильтр. Фильтр может быть необязательным, кстати.</p>
<h3>Словари</h3>
<p>Словарь – это отображение одних элементов в другие. Первые называют ключами, вторые – значениями.</p>
<pre><code>:::python
user_info = {'name': 'Иван', 'level': 2}
print(user_info['name'])  # Иван
</code></pre>
<p>Из словаря можно удалять, менять и добавлять в него элементы:</p>
<pre><code>:::python
user_info = {'name': 'Иван', 'level': 2}
user_info['middle_name'] = 'Иванович'
user_info['name'] = 'Грирогий'
del user_info['level']
print(user_info)  # {'middle_name': 'Иванович', 'name': 'Грирогий'}
</code></pre>
<p>Важный момент про словари: они хранят только отображение одних элементов в других, а порядок элементов не хранят.
В примере выше <code>middle_name</code> был выведен первым, но на это полагаться нельзя.</p>
<p>Ещё у словарей есть несколько важных методов: <code>keys</code>, <code>values</code> и <code>items</code>. Первый возвращает список только ключей, 
второй – список только значений, третий – список пар из ключей и значений. Удобно при итерации по словарю:</p>
<pre><code>:::python
user_info = {'name': 'Иван', 'level': 2}
for key, value in user_info.items():
    print '%s: %s' % (key, value)
# name: Иван
# level: 2
</code></pre>
<h3>Кортежи</h3>
<p>Кортеж выглядит как список, но не совсем. Это скорее структура из C++.
Отличаются от списков тем, что его элементы гетерогенные и тем, что он умеет упаковываться и распаковываться.
Подробнее, например, <a href="https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences">в документации</a>.</p>
<h3>Множества</h3>
<p>Множество – это математическое множество. В нём все элементы уникальные, можно считать пересечение,
проверять на вхождение и выполнять другие операции с множествами. </p>
<p>Один из частых случаев применения множеств – удаление дублей из списка:</p>
<pre><code>:::python
l = [1, 2, 1, 3, 2]
print(list(set(l)))  # [1, 2, 3]
</code></pre>
  <h3><a href="/index.html">На главную</a></h3>

        </div>
      </div>
    </div>

  </body>
</html>