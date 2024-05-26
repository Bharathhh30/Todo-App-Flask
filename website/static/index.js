function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ noteId: noteId }),
    }).then((res) => {
        if (res.status === 200) {
            window.location.href = "/";
        } else {
            alert("Failed to delete the note.");
        }
    });
}
