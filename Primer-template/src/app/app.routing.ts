import { AdminLayoutComponent, AuthLayoutComponent } from "./core";

import { Routes } from "@angular/router";

export const AppRoutes: Routes = [
  {
    path: "",
    redirectTo:"dashboard",
    pathMatch: 'full'
  },
  
  {
    path: "",
    component: AdminLayoutComponent,
    children: [
      {
        path: "dashboard",
        loadChildren: () =>
          import("./dashboard/dashboard.module").then(m => m.DashboardModule),
          data: {
            breadcrumb: "Dashboard"
          }
      },      
      {
        path: "charts",
        loadChildren: () =>
          import("./chartlib/chartlib.module").then(m => m.ChartlibModule),
        data: {
          breadcrumb: "Charts"
        }
      },
      {
        path: "maps",
        loadChildren: () => import("./maps/maps.module").then(m => m.MapModule),
        data: {
          breadcrumb: "Maps"
        }
      },
  
      {
        path: "pages",
        loadChildren: () =>
          import("./pages/pages.module").then(m => m.PagesModule),
          data: {
            brreadcrumb: "Pages"
          }
      }
    ]
  },
  {
    path: "",
    component: AuthLayoutComponent,
    children: [
      {
        path: "session",
        loadChildren: () =>
          import("./session/session.module").then(m => m.SessionModule)
      }
    ]
  },
  {
    path: "**",
    redirectTo: "session/404"
  }
];
