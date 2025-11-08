import 'package:flutter/material.dart';

void main() {
  runApp(MyColumnApp());
}

class MyColumnApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Profile - Thirtho Raj Saha"),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                "Name: Thirtho Raj Saha",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
              SizedBox(height: 20),
              Image.network(
                "https://via.placeholder.com/150", // sample image
                height: 120,
                width: 120,
              ),
              SizedBox(height: 20),
              Text(
                "Email: thirtho@example.com",
                style: TextStyle(fontSize: 18),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
