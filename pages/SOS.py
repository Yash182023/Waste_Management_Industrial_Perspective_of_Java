from twilio.rest import Client
import streamlit as st 

custom_style = """
<style>
    .main {
       background: rgb(2,189,233);
        background: linear-gradient(148deg, rgba(2,189,233,1) 0%, rgba(93,0,255,1) 49%, rgba(2,189,233,1) 100%);
    }

    h1 {
        color: #ffffff;
    }

    p {
        font-weight: 400;
        font-size: 20px;
        color: #ffffff;
        padding-left: 10px;
    }

    .box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 0 0 5px #690021;
    }

    
</style>
"""

st.markdown(custom_style, unsafe_allow_html=True)

# Twilio credentials
account_sid = ''
auth_token = ''
twilio_number = ''
recipient_number = ''  # Update with your recipient's phone number

# Initialize Twilio client
client = Client(account_sid, auth_token)

st.title("Send SOS to MCD")

cont = """
### Purpose of the SOS Feature:

The SOS feature is designed to provide immediate assistance in emergency situations related to pollution or environmental hazards. Users can activate the SOS to quickly report incidents such as highly polluted areas or other environmental emergencies to the appropriate authorities.

### How to Use:

1. **Activate SOS**: If you encounter a highly polluted area or any environmental emergency, simply press the "SOS - Report Emergency" button to send a distress signal.

2. **Custom Message**: You can enter a custom SOS message to provide additional details about the emergency situation.

3. **Confirmation**: After sending the SOS message successfully, you will receive a confirmation message indicating that the SOS has been sent.

4. **Action Taken**: Authorities will be notified about the emergency, and appropriate action will be taken to address the situation.

Remember, the SOS feature is intended for genuine emergency situations. Please use it responsibly and only in case of actual emergencies.
"""

st.markdown(cont,unsafe_allow_html=True)

def send_sos(message_body):
    try:
        # Send SOS SMS
        message = client.messages.create(
            from_=twilio_number,
            body=message_body,
            to=recipient_number
        )
        return message.sid
    except Exception as e:
        st.error(f"Error sending SOS message: {str(e)}")
        return None

# UI components
message_input = "Attention needed! the area is having high solid waste accumullation"

if st.button("Send SOS"):
    # Send SOS message
    sos_message = message_input.strip()
    if sos_message:
        message_sid = send_sos(sos_message)
        if message_sid:
            st.success("SOS Message sent successfully!")
            st.info(f"SOS Message SID: {message_sid}")
    else:
        st.warning("Please enter a valid SOS message.")
