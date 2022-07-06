# src/hypermodern_python/console.py
import textwrap
import locale
import click
import requests


from . import __version__


API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""

    # Get and set locale language
    locale_lang, locale_encoding = locale.getdefaultlocale()
    click.echo(textwrap.fill(locale_lang + " : " + locale_encoding))

    # Language selector
    LANG_SLICE = slice(8,10)

    NEW_URL = list(API_URL)
    NEW_URL[LANG_SLICE] = 'en'
    NEW_URL = ''.join(NEW_URL)

    click.echo(textwrap.fill(NEW_URL))


    with requests.get(NEW_URL) as response:
        try:
            response.raise_for_status()
            data = response.json()

            title = data["title"]
            extract = data["extract"]

            click.secho(title, fg="green")
            click.echo(textwrap.fill(extract))

        except requests.exceptions.HTTPError as err:
            click.secho("HTTP Error", fg="red")
            # click.echo(textwrap.fill(err))
            raise SystemExit(err)


