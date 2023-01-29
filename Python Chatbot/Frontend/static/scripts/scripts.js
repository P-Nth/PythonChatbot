// const { get } = require("express/lib/response");

class ChatClient {
  constructor() {
    this.args = {
      viewToggleIcon: document.querySelector(".opener"),
      chatClient: document.querySelector(".chatclient_container"),
      sendButton: document.querySelector(".send_btn"),
    };

    this.state = false;
    this.messages = [];
  }

  display() {
    const { viewToggleIcon, chatClient, sendButton } = this.args;

    viewToggleIcon.addEventListener("click", () =>
      this.toggleState(chatClient)
    );

    sendButton.addEventListener("click", () =>
      this.onSubmitMessage(chatClient)
    );

    const node = chatClient.querySelector(".input");
    node.addEventListener("keyup", ({ key }) => {
      if (key === "Enter") {
        this.onSubmitMessage(chatClient);
      }
    });
  }

  toggleState(chatClient) {
    this.state = !this.state;

    if (this.state) {
      chatClient.classList.add("unhide");
    } else {
      chatClient.classList.remove("unhide");
    }
  }

  onSubmitMessage(chatClient) {
    let inputField = chatClient.querySelector(".input");
    let inputMessage = inputField.value;
    if (inputMessage === "") {
      return;
    }

    let getMessage = { name: "User", user_message: inputMessage };
    this.messages.push(getMessage);

    fetch("http://127.0.0.1:5000/analy", {
      method: "POST",
      body: JSON.stringify({ user_message: inputMessage }),
      mode: "cors",
      headers: { "Content-type": "application/json" },
    })
      .then((r) => r.json())
      .then((r) => {
        let getSecondMessage = { name: "AI", bot_reply: r.reply };
        this.messages.push(getSecondMessage);
        this.updateReplyText(chatClient);
        inputField.value = "";
      })
      .catch((error) => {
        console.log("Error:", error);
        this.updateReplyText(chatClient);
        inputField.value = "";
      });
  }

  updateReplyText(chatClient) {
    let plainText = "";
    this.messages.slice().forEach(function (item) {
      if (item.name === "User") {
        plainText +=
          '<div class="outgoing"> <div class="actual_msg"> <div class="message" id="actual_msg">' +
          item.user_message +
          '</div> </div> <div class="profile"> <img class="profilepic" src="../static/images/outgoing.png" alt="outgoing profile"/> </div> </div>';
      } else {
        plainText +=
          '<div class="incoming"> <div class="profile"> <img class="profilepic" src="../static/images/incoming.png" alt="incoming profile"/> </div> <div class="actual_msg"> <div class="users_message" id="actual_msg">' +
          item.bot_reply +
          "</div> </div> </div>";
      }
    });

    const messageChats = chatClient.querySelector(".new_view");
    messageChats.innerHTML = plainText;
  }
}

const chatgenerated = new ChatClient();
chatgenerated.display();
