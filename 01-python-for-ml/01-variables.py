

# What is variables?
# - A variable is a name given to a memory location in a program.


# -----------------------------------------
# Example 1 : Basic Variable Demonstration
# -----------------------------------------

COMPANY_NAME = "NVIDIA"
modelVersion = 5.8
connectedUsers = 12000
serverLoad = 71.3
isAIEnabled = True
errorMessage = None 
print("-------NVIDIA----------")
print(COMPANY_NAME)
print(modelVersion)
print(connectedUsers)
print(serverLoad)
print(isAIEnabled)
print(errorMessage)


# -----------------------------------------
# Example 2 : Production Monitoring System
# -----------------------------------------

COMPANY_NAME = "Google"
AI_SYSTEM_NAME = "Gemini"
system_version = 4.5
device_count = 34560
cpu_temperature_celcius = 55.6
gpu_percent = 91.4
average_response_time_ms = 174
maximum_response_time_ms = 200
system_within_safe_limits = average_response_time_ms <= maximum_response_time_ms
critical_alert_message = "No active alerts"

print("----------Gemini-----------")
print("Company Name:", COMPANY_NAME)
print("AI System Name:", AI_SYSTEM_NAME)
print("System version",system_version)
print("Device Count:",device_count)
print("CPU Temperature:",cpu_temperature_celcius)
print("GPU Utilization:",gpu_percent)
print("Average Response Time:",average_response_time_ms)
print("Maximum Response Time:",maximum_response_time_ms)
print("System Operating Safely:",system_within_safe_limits)
print("Critical Alert Status:",critical_alert_message)