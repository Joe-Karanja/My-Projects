import { Injectable } from "@angular/core";
import { TranslateService } from "@ngx-translate/core";

@Injectable()
export class MenuService {
  constructor(public translate: TranslateService) { }

  getAll() {
    return [
      {
        label: this.translate.instant("DASHBOARD"),
        icon: "dashboard",
        items: [
          { link: "/", label: this.translate.instant("HOME") }
        ]
      },
     ];
  }
}
