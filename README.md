# SuperTypist

Pygame-based typing game, a simplified "金山打字通" of python version.

## How to use it

```python
cd superTypist
pip install -r requirements.txt

cd src
python main.py [-h] [--f F]
```

```
usage: main.py [-h] [--f F]

Typing exercice.

optional arguments:
  -h, --help  show this help message and exit
  --f F       path for the text you would like to type
```

## TODO

- [ ] improve efficiency of dynamically rendering text of multiple lines in Pygame.

Welcome **PR** for this task. Note that by now *Pygame has not yet supported newline in text*.

## Result

![animation](animation.gif)