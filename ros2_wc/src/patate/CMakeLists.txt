cmake_minimum_required(VERSION 3.5)
project(patate)

find_package(ament_cmake_python REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)


ament_python_install_package(${PROJECT_NAME})
install(PROGRAMS
  patate/publisher_member_function.py
  patate/subscriber_member_function.py
  patate/mytho_subscriber_member_function.py
  patate/service_member_function.py
  patate/client_member_function.py
  DESTINATION lib/${PROJECT_NAME}
)


ament_export_dependencies(rosidl_default_runtime)
ament_package()
