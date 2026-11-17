#!/usr/bin/env python3


class Bus:
    def mode(self) -> str:
        return "road"


class Train:
    def mode(self) -> str:
        return "rails"


class Bike:
    def mode(self) -> str:
        return "lane"


class Scooter:
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    def __init__(self) -> None:
        self._registry = {}

    def register_kind(self, name: str, cls) -> None:
        self._registry[name] = cls

    def create(self, kind: str):
        return self._registry[kind]()


def main() -> None:
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()

