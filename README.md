# PokeAuth

A helper library for developers using [PokeAuth](https://www.pokeauth.com).

## Installation

```
pip install pokeauth
```

## Getting Started

Make sure you have signed up for a [developer account](https://www.pokeauth.com/developer/register)
before following the steps below.

### User Permissions

Add this image as a button on your website:

![pokeauth button](https://github.com/thisbejim/pokeauth-python/raw/master/pokeauth-button.png)

In your [dashboard](https://www.pokeauth.com/developer/dashboard) you will find a url that looks like this:

```
https://www.pokeauth.com/access/I5ulSrNsYgS034wtO1d0kSswSiu1
```

When users click the PokeAuth button you should send your users to this url. Here the user can decide whether or not to give you
access to their details. If they approve your application they will be sent to your callback url along with their user id:

```
https://www.yourdomain.com/callback?uid=8dH7JM15TRTR6MVPHU7RQLeSgqE2
```

You can use the ```uid``` in this url to request user tokens (I recommend storing them in local storage).

### login

The ```login``` method takes your developer email and password and returns a promise.

```
import pokeauth

poke = pokeauth.login(email, password)
```

### get_user_token

You can retrieve the access tokens of users who have approved your application by passing
their ```uid``` into the ```get_user_token``` method.

The ```get_user_token``` method returns an ```accessToken``` and a ```provider``` (either 'google' or 'ptc').

```
poke = pokeauth.login(email, password)
user = poke.get_user_token(uid)
print(user["accessToken"], user["provider"])
```