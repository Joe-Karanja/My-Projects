import { Component, OnInit } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  providers: [UserService]
})
export class AppComponent implements OnInit{
  register: any;

  constructor(private UserService:UserService){}

  ngOnInit() {
    this.register = {
      username: '',
      password:'',
      email:''

    };
  }
  registerUser(){
    this.UserService.registerNewUser(this.register).subscribe(
      response => {
        alert('User' + this.register.username + 'has been created!')
      },
      error => console.log('error', error)
    );
  }
}
