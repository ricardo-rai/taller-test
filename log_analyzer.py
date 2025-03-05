test = """
[2025-02-20 14:32:10] INFO - Agent Response: "Hello! How can I help you today?"
[2025-02-20 14:33:15] ERROR - Model Timeout after 5000ms
[2025-02-20 14:32:10] INFO - Agent Response: "Hello! How can I help you today?"
[2025-02-20 14:33:15] ERROR - Model Timeout after 5000ms
[2025-02-20 14:34:02] INFO - Agent Response: "I'm sorry, I didn't understand that."
[2025-02-20 14:33:15] ERROR - Model Timeout after 5000ms
[2025-02-20 14:34:02] WARNING - Almost error
"""

def log_analyzer(log: str) -> str:
    types = {}
    messages = {}
    errors = {}
    warnings = {}
    for line in log.splitlines():
        message_splited_time = line.split("] ", 1)
        if len(message_splited_time) >= 2:
            message_splited_type = message_splited_time[1].split(" - ")
            if message_splited_type[0] not in types:
                types[message_splited_type[0]] = 1
            else:
                types[message_splited_type[0]] += 1
            if "Agent Response" in message_splited_type[1]:
                message_from_agent = message_splited_type[1].split("Agent Response: ")
                if message_from_agent[1] not in messages:
                    messages[message_from_agent[1]] = 1
                else:
                    messages[message_from_agent[1]] += 1
            else:
                if message_splited_type[0] == "ERROR":
                    message_error_warning = message_splited_type[1]
                    if message_error_warning not in errors:
                        errors[message_error_warning] = 1
                    else:
                        errors[message_error_warning] += 1
                elif message_splited_type[0] == "WARNING":
                    message_error_warning = message_splited_type[1]
                    if message_error_warning not in warnings:
                        warnings[message_error_warning] = 1
                    else:
                        warnings[message_error_warning] += 1

    print("Log Summary:")
    for k, v in types.items():
        print(f"- {k} messages: {v}")

    print("\nTop 3 AI Responses:")
    for k, v in enumerate(sorted(messages.items(), key=lambda item: item[1], reverse=True)[:3]):
        print(f"{k+1} {v[0]} ({v[1]} times)")
    
    print("\nMost Common Errors:")
    for k, v in enumerate(sorted(errors.items(), key=lambda item: item[1], reverse=True)[:3]):
        print(f"{k+1} {v[0]} ({v[1]} times)")
    
    



log_analyzer(test)