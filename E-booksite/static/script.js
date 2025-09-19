// List of books
const books = [
    /*{ title: "Book 1", file: "books/book1.pdf", cover: "images/book1.jpg" },
    { title: "Book 2", file: "books/book2.pdf", cover: "images/book2.jpg" }*/
];

const bookList = document.getElementById("book-list");
const pdfModal = document.getElementById("pdfModal");
const pdfViewer = document.getElementById("pdfViewer");
const closeModal = document.getElementById("closeModal");

// Display books
books.forEach(book => {
    const bookDiv = document.createElement("div");
    bookDiv.className = "book";

    bookDiv.innerHTML = `
        <img src="${book.cover}" alt="${book.title}">
        <h3>${book.title}</h3>
        <button onclick="openPDF('${book.file}')">Read Online</button>
        <a href="${book.file}" download>Download</a>
    `;

    bookList.appendChild(bookDiv);
});

// Open PDF in modal
function openPDF(file) {
    pdfViewer.src = file;
    pdfModal.style.display = "block";
}

// Close modal
closeModal.onclick = () => {
    pdfModal.style.display = "none";
    pdfViewer.src = "";
}

// Close modal if click outside iframe
window.onclick = (e) => {
    if (e.target === pdfModal) {
        pdfModal.style.display = "none";
        pdfViewer.src = "";
    }
}