"""
STRING API client using httpx.
"""

from .client import Client, __version__

__all__ = ["__version__", "Client"]

identity = ""


def map(identifiers: list[str], species: int):
    with Client(identity=identity) as client:
        return (
            client.map(identifiers=identifiers, species=species)
            .raise_for_status()
            .json()
        )


def network(identifiers: list[str], species: int):
    with Client(identity=identity) as client:
        return (
            client.network(identifiers=identifiers, species=species)
            .raise_for_status()
            .json()
        )


def interaction_partners(identifiers: list[str], species: int):
    with Client(identity=identity) as client:
        return (
            client.interaction_partners(identifiers=identifiers, species=species)
            .raise_for_status()
            .json()
        )


def homology(identifiers: list[str], species: int):
    with Client(identity=identity) as client:
        return (
            client.homology(identifiers=identifiers, species=species)
            .raise_for_status()
            .json()
        )


def version():
    with Client(identity=identity) as client:
        return client.version()
