import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Crops } from './crops';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http:HttpClient) { }
  url:string="http://127.0.0.1:8000/detect";
  getCropsAnalysis(){
    return this.http.get<Crops[]>(this.url);
  }
}
