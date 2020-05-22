# Selenium wrapper

The selenium wrapper can be used as a general purpose framework allowing for an easier, faster and less error prone way
to interact with selenium.

# How to
* Get an element:  
`element = find_element((<selector type>, <selector>))`  
or  
`element = find_element(<key in the selector dictionary>)`
  
* Click on an element:  
`element.click()`

* Get the text of an element:  
`text = element.text`

* Write text:  
`element.send_keys("some example text")`


# Find element
* Finds the element on the webpage and returns the selenium element object
* locator  
  * Takes in a locator element. It can either be a string or a tuple.
string: Must be a string, that is contained in the selector dictionary as a key
tuple: Must be in the format of `(<selector type>, <selector>)`, for example `("id", "first")`
* timeout  
  * Sets the timeout for how long it will wait for this element to appear before it throws an
exception.
* suppress_error  
  * If set to True, when the element is not found, the function returns None and moves on
instead of crashing.
  * This can be useful when checking if an element exists:
```python
  # Check if an element is present:
  element = find_element(("xpath", "//some/example/xpath"), timeout=5, supressError=True)
  if element is not None:
  # Is present
  else:
  # Is not present
```

