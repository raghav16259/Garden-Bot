# Garden-Bot
IED Project 
This bot is essentially a mobile cart with water, mechanical arm, camera, ultrasonic sensor, etc.It moves freely (chooses the direction randomly), detects an object and if the object is a plant (done using image recognition library), checks the moisture of the pot, and adds water to the pot plant if the moisture content of the soil is low. It is integrated with the internet to check whether it has rained in the past few days to make a smarter decision for watering. As it moves autonomously, it can water all the pots in a garden – essentially doing the job of a smart gardener.

Components: MoistureSensor, Ultrasonic Sensor, Webcam, five motors(four for wheels and one for water pump), One servo motor (for arm), H-Bridge for controlling DC motor
Platform and Code: Raspberry Pi, with about 500 LOC of Python.
