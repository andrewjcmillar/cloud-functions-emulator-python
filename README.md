# GCP Cloud Functions Python Emulator

## Usage
Copy the `emulator.py` file into the same level as your `main.py` file.

In a virtual environment install all the requirements for your project as well as the `click` and `flask` requirements defined in `requirements.txt` in this repository.

To run a cloud function on a HTTP endpoint locally use the command

```bash
python emulator.py {function_name}
```

Where `function_name` is the name of the function you want to emulate in `main.py`

You can also specify the route and port that this will run on
```bash
python emulator.py {function_name} --route route_name --port 8002
```

By default you'll find your function at `http://localhost:3001/`