# micro:bit tools

> Some tools to make your life with the micro:bit a little easier.

## VS Code Tooling
The default build task is set to flash the micro:bit with the code in [bit.py](bit.py). If the micro:bit cannot be found, add a location to flash to:

```json
{
    ...
    "command": "uflash bit.py /mnt/d/",
    ...
}
```

You can run the default build tool using `CTRL+F7` or by typing `CTRL+SHIFT+P` and typing `Tasks: Run Build Task`.
