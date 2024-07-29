import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display_console(self) -> None:
        print(self.content)

    def display_reverse(self) -> None:
        print(self.content[::-1])

    def print_book_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_book_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def serialize(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return self.serialize_json()
        elif serialize_type == "xml":
            return self.serialize_xml()

        raise ValueError(f"Unknown serialize type: {serialize_type}")

    def serialize_json(self) -> json:
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_xml(self) -> json:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            try:
                getattr(book, f"display_{method_type}")()
            except AttributeError:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            try:
                getattr(book, f"print_book_{method_type}")()
            except AttributeError:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "console"), ("serialize", "xml")]))
