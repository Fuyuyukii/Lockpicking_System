<h1 align="center"> 🔐 Lockpicking System 🔑 </h1>

### Project Description
This project is a lockpicking mini-game by text, that you should hit the hidden numbers in each spring,<br>
with "springs" i meant, every spring that exists inside of padlocks or locks<br>
which will be represented by [X].The 'X' represents the hidden number of this spring,<br>
when you hit the number, the [X] will turn in green and will appear an `*click*` on console.<br>
hitting all number, you will be able to open the container.
### Features
* Lock order<br>
  *This feature when activated, will place an order to unlock the lock,<br>
  for example you wont be able to unlock 1-2-3, but 3-1-2 for example,<br>
  where those numbers are the order to unlock.*
* Fake clicks<br>
  *This feature will include fake clicks, meaning, even you get the number wrong there will be a probability of `*click*`<br>
  will appear on your screen, but fake click will only have the probability if this spring have the mod of "fake click".<br>
  obs: the probability is given by a ratio between your lockpicking skill level and the amount of springs.*
* Visible springs<br>
  *You won't be able to see the all springs, the amount of springs you can see is given by your lockpicking skill level.<br>
  example:[X][X][X](visible springs) + [X][X](invisible springs) where lockpicking lvl = 3 and amount of springs = 5.*
* Lock durability<br>
  *All locks have 100 base durability, but when you try to open the container without hitting all the springs, it will<br>
  damage the lock, if the lock's durability reaches 0, the minigame will end.<br>
  obs: how more springs not hitted, more damage the lock will receive.*
### How to use
when you open the code, you just have two things that you can change,<br>
lockpicking skill, what is the level of lockpicking skill.<br>
and the arguments of generate_lock.<br>
<br>
generate_lock(1,2,3,4)<br>
1 - is the quantity of springs that the lock will have.(int)<br>
2 - the amplitude of the X can be, for examplo if it = 10, so a number 0-10 can be generate.(int)<br>
3 - the quantity of fake clicks, it not set where they are, just the qauntity.(int)<br>
4 - if the lock have an order(boolean)[default=false]<br>
example=generate_lock(5, 10, 1, True)
### COMMANDS
- put a number until this match of the number of spring<br>
- "Open" you will try to open<br>
- "next" to go to next spring<br>
- "previous" to go to previous spring<br>
- "Exit" to exit<br>
