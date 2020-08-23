## **Об экзамене**

Эказамены в Академию больших данных от MAIL.RU (https://data.mail.ru/) - это первая попытка поступления на курсы подобнго рода.
До этого за плечами всевозможные курсы от Корпоративного университета Сбербанка, в т.ч. по анализу данных на Python и машинному обучению.
В MADE, как и в ШАД обучение более основателное и фундаментальное.

В экзаменационном сете у них:
- экзамен по математике (в этом году, считаю, был уклон на олимпиадную математику), 4 часа на 10 задач.
- экзамен по машинному обучению (задача на бинарную классификацию, задача на построение рекомендательной системы), на это выделено 2 недели
- экзамен по программированию, 24 часа на 6 задач.

Судя по обсуждению в чате участников, наибольший интерес вызвала задача "Cломанный HTML", свой вариант решения которой я и решил опубликовать.


## **Задачи**
### **Немножко сломанный HTML**

**Условия**

`Тесты с оценкой в 50: документ может быть сломан только добавлением лишнего закрывающего тега
Тесты с оценкой в 100: документ может быть сломан произвольным образом (нарушиться может любое свойство, из описанных выше).`

Было замечено, что у разработчиков веб-сайтов очень частая ошибка - это случайное добавление одного лишнего тега в html документ, который делает его некорректным. В рамках кампании по улучшению качества разрабатываемого программного обеспечения, было принято решение о разработке программы для автоматического исправления подобного рода ошибок. 

HTML-документ - это последовательность открывающих и закрывающих тегов. Открывающий тег - это последовательность английских букв, обособленных треугольными скобками с двух сторон. Пример - <html> . Закрывающий тег - это тоже самое, что и открывающих тег, но с дополнительным символом слеша после левой треугольной скобки. Пример - </html>. 

Тег </X> является закрывающим тегом к <Y>, если X = Y (<Y> тогда - это открывающих тег для </X>). Все теги регистронезависимые - это означает, что <HTML> и <html> - это один и тот же тег.

Каждый тег определяет элемент на странице. Элемент может быть пустой - это означает, что после открывающего тега элемента, сразу стоит закрывающий. Элементы могут быть вложенными друг в друга. Это означает, что между открывающим и закрывающим тегом находятся еще какое-то количество элементов. 

При этом для корректного документа должны выполняться следующие свойства:

Для одного открывающего тега может быть ровно один закрывающий тег.
Для одного закрывающего тега может быть ровно один открывающий тег.
Элементы могут быть только строго вложенными друг в друга - перехлест элементов запрещен (например <x><y></x></y>).
HTML-документ считается сломанным, если какое-то из этих свойств нарушается. Например, для данного тега не нашлось открывающего\закрывающего тега или существует перехлест в тегах.

Для заданного HTML документа необходимо выяснить, является ли он сломанным или нет. Если документ является сломанным, то нужно узнать, не был ли он сломан случайно разработчиком (разработчик мог случайно добавить один лишний тег). То есть, если документ сломан, нужно проверить, можно ли его починить, удалив ровно один тег.

_Ограничения_
  
Количество строк в документе h: 1 <= h <= 10^6.
Количество букв внутри тега k: 1 <= k <= 100.
В последнем примере два открывающих тега <TAG>, у которых нет закрывающих. Таким образом этот документ нельзя починить удалением какого-то одного тега.
  
_Формат входных данных_
  
Первая строка содержит одно целое число x — количество наборов входных данных. После следуют x наборов данных. 
Первая строка набора данных содержит одно число s - количество тегов в документе.
Следующие s строк — это последовательность тегов в документе. По одному тегу на каждой строке.

_Формат выходных данных_
  
Для каждого набора данных необходимо определить, насколько сломан документ.
Если документ корректен, необходимо вывести слово `CORRECT`.
Если документ некорректен, но при этом его можно починить, удалив ровно один тег — вывести `ALMOST <TAG>` . Где `<TAG>` - это название тега, который необходимо удалить для починки. `<TAG>` необходимо выводить в верхнем регистре.
Если документ некорректен и при этом его нельзя починить указанным способом — вывести `INCORRECT`.
  
**Решение**

Основная идея заключается в том, чтобы сформировать 2 списка: в первом будут храниться исключительно открывающие теги, а во вором - плохие (ошибочные). При добалении очередного тега, происходит проверка, открыающийся ли он или закрывающийся. Если он открывающийся, то добавляется в первый список. Если тег закрывающийся, то или происходит удаление последнего тега в первом списке (после сравнения, одинаковые ли теги) или он добавляется во второй список, как ошибочный (ведь в этом случае, он не может ничего закрыть).
Если последовательность тегов верная, то в первом теге в конце исполнения программы не должно остаться ни одного тега, если в первом или втором списке по одному тегу, то это вариант `ALMOST <TAG>` (ситуация, когда можно удалить 1 тег), в остальных случаях - `INCORRECT`