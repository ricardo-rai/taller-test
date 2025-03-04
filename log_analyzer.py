test = """
[2025-02-20 14:32:10] INFO - Agent Response: "Hello! How can I help you today?"
[2025-02-20 14:33:15] ERROR - Model Timeout after 5000ms
[2025-02-20 14:34:02] INFO - Agent Response: "I'm sorry, I didn't understand that."
"""

def log_analyzer(log: str) -> str:
    type = {}
    message = {}
    error_warning = {}
    for line in log.splitlines():
        message_splited_time = line.split("] ", 1)
        if len(message_splited_time) >= 2:
            message_splited_type = message_splited_time[1].split(" - ")
            if message_splited_type[0] not in type:
                type[message_splited_type[0]] = 1
            else:
                type[message_splited_type[0]] += 1
            if "Agent Response" in message_splited_type[1]:
                message_from_agent = message_splited_type[1].split("Agent Response: ")
                if message_from_agent[1] not in message:
                    message[message_from_agent[1]] = 1
                else:
                    message[message_from_agent[1]] += 1
            else:
                message_error_warning = message_splited_type[1]
                if message_error_warning[1] not in error_warning:
                    error_warning[message_error_warning] = 1
                else:
                    error_warning[message_error_warning] += 1

    
    print(type)
    print(message)
    print(error_warning)

    print(f"""

    """)
    



log_analyzer(test)