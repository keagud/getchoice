# getchoice

A simple library to allow a user to select from a list of options on the command line. Like [pick](https://github.com/wong2/pick), but with two major differences:
 
- `getchoice` is intended for use alongside [python prompt toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit); its output can be styled using PPT-style `(styling, text)` format.
- `getchoice` does not use `curses`, and does not clear the screen when used.


```python 

from getchoice import ChoicePrinter

choice_printer = ChoicePrinter(normal_style="green italic")


items = [ 
  ("first display", "first object"), 
  ("second display", "second object"), 
  ("third display", "third object")
  ]

choice_printer.getchoice(items)
```

This displays an interactive prompt menu for the choices, that the user can navigate with the arrow or j/k keys, and select and item with space or enter. `choice_printer.getchoice()` returns a tuple of the form `(selected_index: int, selected_object)`

