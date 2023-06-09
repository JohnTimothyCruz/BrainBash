import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { postDeck } from "../../store/decks";
import "./CreateDeckModal.css"

const CreateDeckModal = ({ props }) => {
    const dispatch = useDispatch();
    const [name, setName] = useState("")
    const [processing, setProcessing] = useState(false)
    const { closeModal } = useModal();
    const [chosenClass, user_id] = props;

    const handleSubmit = (e) => {
        e.preventDefault();

        setProcessing(true)

        dispatch(postDeck(name, chosenClass?.id, user_id))
            .then(closeModal)
    }

    return (
        <div id="create-deck-modal">
            <i id="close-create-deck-modal-button" className="fa-solid fa-xmark fa-2xl" onClick={() => closeModal()} />
            <h2 id="create-deck-prompt">Create New Deck</h2>
            <h3 id="create-deck-explaination">A Deck is a subset of Flashcards in a Class, similar to chapters in a book</h3>
            <form id="create-deck-form" onSubmit={(e) => handleSubmit(e)}>
                <input
                    id="create-deck-title-input"
                    placeholder="e.g. Cell Division, Capitals of Asia"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <p id="create-deck-input-text">Enter the title of your new deck above</p>
                {name?.length > 250 &&
                    <div id="create-deck-error">Sorry, but your deck title must be less than 250 characters.</div>
                }
                <button
                    id="create-deck-form-button"
                    disabled={!name || name?.length > 250 || processing}
                >C O N T I N U E</button>
            </form>
        </div>
    )
}

export default CreateDeckModal
