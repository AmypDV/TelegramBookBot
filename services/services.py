
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    sep = ',.!:;?'
    new_text = text[start:start+page_size]
    len_new_text = len(new_text)
    sep_iter = ((len_new_text - n, i) for n, i in enumerate(new_text[::-1], start=1) if i in sep)
    for n, i in sep_iter:
        if len(text) > n + start + 1 and text[n + start + 1] in sep:
            continue
        new_text = new_text[:n + 1]
        return new_text, len(new_text)



BOOK: dict[int, str] = {}
PAGE_SIZE = 1050



def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    start, n_page = 0, 0
    l_text = len(text)
    while start < l_text:
        n_page += 1
        text_page, len_page = _get_part_text(text, start, PAGE_SIZE)
        start += len_page
        BOOK[n_page] = text_page.lstrip()

prepare_book('book.book.txt')