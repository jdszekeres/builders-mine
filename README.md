# builders-mine

## minecraft like game using Pyglet

### install

```bash
git clone https://github.com/jdszekeres/builders-mine.git
cd builders-mine
pip install -r requirements.txt
python3 main.py
```

### server

builders mine also has a server to lighten the load on your computer. To host the server instance you need to run server.py with Flask installed

```bash
pip install Flask
```

to load the game from the server choose

```plain
start Game>Load Game>local server
```
if you reccive a urllib error
```python
requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=5000): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fbcafa72370>: Failed to establish a new connection: [Errno 61] Connection refused'))
```
 it is because you server is not on or working run it with
```bash
python server.py
```

it will not load if [localhost:500](https://127.0.0.1:5000)

### screenshots
![](screenshots/tree.png)
![](screenshots/stair.png)
![](screenshots/house1.png)
![](screenshots/house2.png)
![](screenshots/main.png)
![](screenshots/game-choose.png)
![](screenshots/day-night.png)
