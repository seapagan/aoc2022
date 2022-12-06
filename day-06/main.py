"""Advent of Code 2022, 5th Dec."""


def load_data() -> str:
    with open("input-data.txt") as f:
        data = f.read()
        return data


def find_answer(signal: str, width: int) -> int | None:
    """Find the packet marker position for the input signal."""
    for index in range(len(signal)):
        sample = signal[index : index + width]
        if len(sample) == len(set(sample)):
            return index + width
    return None


signal = load_data()

packet_marker_index = find_answer(signal, 4)
message_index = find_answer(signal, 14)
print(f"Packet Index is {packet_marker_index}")
print(f"Message Index is {message_index}")
